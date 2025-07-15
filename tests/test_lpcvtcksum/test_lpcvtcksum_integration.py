#!/usr/bin/env python3
"""
Integration tests for lpcvtcksum script.

This test validates the integration aspects of the lpcvtcksum script,
including script execution, argument handling, and file system interactions.
"""

from sys import executable, path
from tempfile import mkdtemp
from shutil import rmtree
from unittest import TestCase
from subprocess import run
from pathlib import Path

# Add the scripts directory to Python path to import lpcvtcksum functionality
script_dir = Path(__file__).parent.parent / "scripts"
path.insert(0, str(script_dir))

class TestLpcVtcksumIntegration(TestCase):
    """Integration tests for lpcvtcksum script."""
    
    def setUp(self):
        """Set up integration test fixtures."""
        self.script_path = script_dir / "lpcvtcksum"
        self.test_dir = Path(mkdtemp())
    
    def tearDown(self):
        """Clean up integration test fixtures."""
        rmtree(self.test_dir, ignore_errors=True)
    
    def test_script_executable(self):
        """Test that the script is executable and has correct shebang."""
        # Check if file exists
        self.assertTrue(self.script_path.exists(), "lpcvtcksum script not found")
        
        # Check shebang
        first_line = self.script_path.read_text().splitlines()[0].strip()
        self.assertEqual(first_line, "#!/usr/bin/env python3", "Script should use python3 shebang")
    
    def test_help_behavior(self):
        """Test script behavior when called without arguments."""
        result = run([executable, str(self.script_path)], capture_output=True, text=True)
        
        # Script should fail when called without arguments
        self.assertNotEqual(result.returncode, 0, "Script should fail when called without arguments")


if __name__ == '__main__':
    import unittest
    unittest.main()
