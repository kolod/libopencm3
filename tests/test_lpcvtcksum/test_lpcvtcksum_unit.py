#!/usr/bin/env python3
"""
Unit tests for lpcvtcksum script.

This test validates the vector table checksum computation for LPC43xx
and other NXP ARM microcontrollers.
"""

from sys import executable, path
from struct import unpack, pack, error
from tempfile import mkdtemp
from shutil import rmtree
from unittest import TestCase
from subprocess import run
from pathlib import Path

# Add the scripts directory to Python path to import lpcvtcksum functionality
script_dir = Path(__file__).parent.parent.parent / "scripts"
path.insert(0, str(script_dir))

class TestLpcVtcksum(TestCase):
    """Test cases for lpcvtcksum functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.lpcvtcksum_script = script_dir / "lpcvtcksum"
        self.test_dir = Path(mkdtemp())
        
    def tearDown(self):
        """Clean up test fixtures."""
        rmtree(self.test_dir, ignore_errors=True)
    
    def create_test_binary(self, vectors, additional_data=b''):
        """Create a test binary file with given vector table."""
        test_file = self.test_dir / "test_firmware.bin"
        
        test_file.write_bytes(
            pack('<IIIIIIII', *vectors) + additional_data
        )
        
        return str(test_file)
    
    def read_binary_vectors(self, filename):
        """Read the vector table from a binary file."""
        file_path = Path(filename)
        raw_vectors = file_path.read_bytes()[:32]
        return list(unpack('<IIIIIIII', raw_vectors))
    
    def calculate_expected_checksum(self, vectors):
        """Calculate the expected checksum for given vectors."""
        checksum_sum = sum(vectors[:7])  # Sum first 7 vectors
        return 1 + (0xffffffff ^ (0xffffffff & checksum_sum))
    
    def test_checksum_calculation_simple(self):
        """Test checksum calculation with simple vector values."""
        # Create test vectors (first 7 are meaningful, 8th will be checksum)
        test_vectors = [
            0x20000400, 0x00000101, 0x00000102, 0x00000103,
            0x00000104, 0x00000105, 0x00000106, 0x00000000
        ]
        
        test_file = self.create_test_binary(test_vectors)
        
        # Run lpcvtcksum
        result = run(
            [executable, str(self.lpcvtcksum_script), test_file], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 0, f"Script failed: {result.stderr}")
        
        # Read back the modified file
        modified_vectors = self.read_binary_vectors(test_file)
        
        # Calculate expected checksum
        expected_checksum = self.calculate_expected_checksum(test_vectors)
        
        # Verify the checksum was calculated correctly
        self.assertEqual(modified_vectors[7], expected_checksum,
                        f"Checksum mismatch: got 0x{modified_vectors[7]:08x}, "
                        f"expected 0x{expected_checksum:08x}")
        
        # Verify other vectors weren't modified
        for i in range(7):
            self.assertEqual(modified_vectors[i], test_vectors[i],
                           f"Vector {i} was modified unexpectedly")
    
    def test_checksum_calculation_realistic(self):
        """Test checksum calculation with realistic ARM vector values."""
        # Realistic ARM vector table values
        test_vectors = [
            0x20008000,  # Initial stack pointer
            0x00000121,  # Reset vector
            0x00000141,  # NMI vector
            0x00000161,  # Hard fault vector
            0x00000181,  # Memory management fault
            0x000001A1,  # Bus fault vector
            0x000001C1,  # Usage fault vector
            0x00000000   # Reserved (checksum will go here)
        ]
        
        test_file = self.create_test_binary(test_vectors)
        
        # Run lpcvtcksum
        result = run(
            [executable, str(self.lpcvtcksum_script), test_file], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 0, f"Script failed: {result.stderr}")
        
        # Read back and verify
        modified_vectors = self.read_binary_vectors(test_file)
        expected_checksum = self.calculate_expected_checksum(test_vectors)
        
        self.assertEqual(modified_vectors[7], expected_checksum)
        
        # Verify checksum output message
        self.assertIn("computed vector table checksum:", result.stdout)
        self.assertIn(f"0x{expected_checksum:08x}", result.stdout)
    
    def test_padding_functionality(self):
        """Test that the script correctly pads files to 4096-byte boundaries."""
        # Create a small test file
        test_vectors = [0x20000400, 0x101, 0x102, 0x103, 0x104, 0x105, 0x106, 0x00]
        additional_data = b'A' * 100  # Add 100 bytes of data
        
        test_file = self.create_test_binary(test_vectors, additional_data)
        test_file_path = Path(test_file)
        
        # Get original size
        original_size = test_file_path.stat().st_size
        
        # Run lpcvtcksum
        result = run(
            [executable, str(self.lpcvtcksum_script), test_file], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 0)
        
        # Check that file size is now a multiple of 4096
        new_size = test_file_path.stat().st_size
        self.assertEqual(new_size % 4096, 0, f"File size {new_size} is not a multiple of 4096")
        self.assertGreaterEqual(new_size, original_size, "File size should not decrease")
    
    def test_file_not_found(self):
        """Test behavior when input file doesn't exist."""
        nonexistent_file = self.test_dir / "nonexistent.bin"
        
        result = run(
            [executable, str(self.lpcvtcksum_script), str(nonexistent_file)], 
            capture_output=True, text=True
        )
        
        self.assertNotEqual(result.returncode, 0, "Script should fail for nonexistent file")
    
    def test_zero_vectors(self):
        """Test checksum calculation with all-zero vectors."""
        test_vectors = [0, 0, 0, 0, 0, 0, 0, 0]
        test_file = self.create_test_binary(test_vectors)
        
        result = run(
            [executable, str(self.lpcvtcksum_script), test_file], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 0)
        
        modified_vectors = self.read_binary_vectors(test_file)
        
        # For all-zero vectors: sum=0, checksum = (1 + (0xffffffff ^ 0)) & 0xffffffff = 0
        expected_checksum = (1 + (0xffffffff ^ 0)) & 0xffffffff
        
        self.assertEqual(modified_vectors[7], expected_checksum)
    
    def test_maximum_values(self):
        """Test checksum calculation with maximum 32-bit values."""
        test_vectors = [0xffffffff] * 7 + [0]
        test_file = self.create_test_binary(test_vectors)
        
        result = run(
            [executable, str(self.lpcvtcksum_script), test_file], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 0)
        
        modified_vectors = self.read_binary_vectors(test_file)
        expected_checksum = self.calculate_expected_checksum(test_vectors)
        
        self.assertEqual(modified_vectors[7], expected_checksum)
    
    def test_preserves_additional_data(self):
        """Test that additional data beyond the vector table is preserved."""
        test_vectors = [0x20000400, 0x101, 0x102, 0x103, 0x104, 0x105, 0x106, 0x00]
        test_data = b"Hello, World! This is test data that should be preserved."
        
        test_file = self.create_test_binary(test_vectors, test_data)
        
        # Run lpcvtcksum
        result = run(
            [executable, str(self.lpcvtcksum_script), test_file], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 0)
        
        # Read the file and check that our test data is still there
        test_file_path = Path(test_file)
        file_data = test_file_path.read_bytes()
        preserved_data = file_data[32:32+len(test_data)]
            
        self.assertEqual(preserved_data, test_data, "Additional data was not preserved correctly")

    def test_no_arguments_usage_message(self):
        """Test that running without arguments shows usage message."""
        result = run(
            [executable, str(self.lpcvtcksum_script)], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 1)
        self.assertIn("Usage: python lpcvtcksum firmware.bin", result.stdout)
        self.assertIn("Compute and insert the vector table checksum", result.stdout)
        self.assertIn("LPC43xx and some other NXP ARM microcontrollers", result.stdout)

    def test_too_many_arguments(self):
        """Test that running with too many arguments shows usage message."""
        result = run(
            [executable, str(self.lpcvtcksum_script), "file1.bin", "file2.bin"], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 1)
        self.assertIn("Usage: python lpcvtcksum firmware.bin", result.stdout)

    def test_file_not_found_error(self):
        """Test proper error handling when file doesn't exist."""
        nonexistent_file = self.test_dir / "does_not_exist.bin"
        
        result = run(
            [executable, str(self.lpcvtcksum_script), str(nonexistent_file)], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 1)
        self.assertIn("Error: File", result.stdout)
        self.assertIn("not found", result.stdout)

    def test_file_too_small_error(self):
        """Test proper error handling when file is too small for vector table."""
        small_file = self.test_dir / "small.bin"
        
        # Create a file smaller than 32 bytes
        small_file.write_bytes(b"small file content")  # Only 18 bytes
        
        result = run(
            [executable, str(self.lpcvtcksum_script), str(small_file)], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 1)
        self.assertIn("Error: File", result.stdout)
        self.assertIn("is too small", result.stdout)
        self.assertIn("needs at least 32 bytes", result.stdout)

    def test_success_message(self):
        """Test that successful processing shows success message."""
        test_vectors = [0x20001000, 0x201, 0x202, 0x203, 0x204, 0x205, 0x206, 0x0]
        test_file = self.create_test_binary(test_vectors)
        test_file_path = Path(test_file)
        
        result = run(
            [executable, str(self.lpcvtcksum_script), test_file], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("computed vector table checksum:", result.stdout)
        self.assertIn("Successfully processed", result.stdout)
        self.assertIn(test_file_path.name, result.stdout)

    def test_pathlib_functionality(self):
        """Test that pathlib-based file operations work correctly."""
        # This test ensures the pathlib migration works
        test_vectors = [0x20002000, 0x301, 0x302, 0x303, 0x304, 0x305, 0x306, 0x0]
        test_file = self.create_test_binary(test_vectors)
        
        # Use a path with special characters to test pathlib robustness
        special_name = self.test_dir / "test file with spaces.bin"
        test_file_path = Path(test_file)
        special_name.write_bytes(test_file_path.read_bytes())
        
        result = run(
            [executable, str(self.lpcvtcksum_script), str(special_name)], 
            capture_output=True, text=True
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("Successfully processed", result.stdout)

    def test_readonly_file_error(self):
        """Test proper error handling when file is read-only."""
        test_vectors = [0x20003000, 0x401, 0x402, 0x403, 0x404, 0x405, 0x406, 0x0]
        test_file = self.create_test_binary(test_vectors)
        test_file_path = Path(test_file)
        
        # Make file read-only
        import stat
        test_file_path.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        
        result = run(
            [executable, str(self.lpcvtcksum_script), test_file], 
            capture_output=True, text=True
        )
        
        # Should fail with permission error
        self.assertEqual(result.returncode, 1)
        self.assertIn("Error: Unable to open or read file", result.stdout)

    def test_write_permission_error(self):
        """Test proper error handling when file cannot be written to."""
        test_vectors = [0x20004000, 0x501, 0x502, 0x503, 0x504, 0x505, 0x506, 0x0]
        test_file = self.create_test_binary(test_vectors)
        test_file_path = Path(test_file)
        
        # Make the parent directory read-only to prevent writing
        import stat
        import os
        
        # On Windows, we need a different approach since making directories read-only
        # doesn't prevent file writing in the same way as Unix systems
        if os.name == 'nt':  # Windows
            # Create a file in a location that should cause write permission issues
            # We'll try to make the file itself read-only after opening
            original_mode = test_file_path.stat().st_mode
            
            try:
                # Make file read-only
                test_file_path.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
                
                result = run(
                    [executable, str(self.lpcvtcksum_script), test_file], 
                    capture_output=True, text=True
                )
                
                # Should fail with write permission error
                self.assertEqual(result.returncode, 1)
                # Check for the specific error message format with filename
                self.assertTrue(
                    f"Error: Unable to write to file '{test_file}'" in result.stdout or
                    f"Error: Unable to open or read file '{test_file}'" in result.stdout,
                    f"Unexpected error message: {result.stdout}"
                )
                
            finally:
                # Restore original permissions for cleanup
                try:
                    test_file_path.chmod(original_mode)
                except:
                    pass  # Ignore cleanup errors
                    
        else:  # Unix-like systems
            # Make parent directory read-only
            parent_dir = test_file_path.parent
            original_mode = parent_dir.stat().st_mode
            
            try:
                # Remove write permission from parent directory
                parent_dir.chmod(stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
                
                result = run(
                    [executable, str(self.lpcvtcksum_script), test_file], 
                    capture_output=True, text=True
                )
                
                # Should fail with write permission error
                self.assertEqual(result.returncode, 1)
                # Check for the specific error message format with filename
                self.assertTrue(
                    f"Error: Unable to write to file '{test_file}'" in result.stdout or
                    f"Error: Unable to open or read file '{test_file}'" in result.stdout,
                    f"Unexpected error message: {result.stdout}"
                )
                
            finally:
                # Restore original permissions for cleanup
                try:
                    parent_dir.chmod(original_mode)
                except:
                    pass  # Ignore cleanup errors

    def test_main_function_guard(self):
        """Test that the script can be imported without executing main code."""
        # Test importing the script as a module
        import importlib.util
        import sys
        import tempfile
        import shutil
        
        # Save original argv to restore later
        original_argv = sys.argv[:]
        
        try:
            # Set safe argv to avoid triggering main() execution issues
            sys.argv = ['lpcvtcksum']
            
            # Create a temporary copy with .py extension for import testing
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
                temp_py_path = Path(temp_file.name)
                
            # Copy the script content to the .py file
            original_content = self.lpcvtcksum_script.read_text()
            temp_py_path.write_text(original_content)
            
            try:
                spec = importlib.util.spec_from_file_location("lpcvtcksum", str(temp_py_path))
                if spec is None or spec.loader is None:
                    self.skipTest("Could not create module spec - this is a platform limitation")
                
                lpcvtcksum_module = importlib.util.module_from_spec(spec)
                
                # This should not execute the main code due to if __name__ == "__main__" guard
                spec.loader.exec_module(lpcvtcksum_module)
                
                # Verify the main function exists and is callable
                self.assertTrue(hasattr(lpcvtcksum_module, 'main'))
                self.assertTrue(callable(getattr(lpcvtcksum_module, 'main')))
                
            finally:
                # Clean up the temporary file
                try:
                    temp_py_path.unlink()
                except:
                    pass  # Ignore cleanup errors
                
        finally:
            # Restore original argv
            sys.argv = original_argv


if __name__ == '__main__':
    import unittest
    unittest.main()
