# LPC Vector Table Checksum Tests

This directory contains tests for the `lpcvtcksum` script, which computes and inserts vector table checksums required for booting LPC43xx and other NXP ARM microcontrollers.

## Test Structure

The tests have been split into separate files for better organization and maintainability:

### Test Files

- **`test_lpcvtcksum_unit.py`** - Unit tests for core functionality
  - Checksum calculation with various vector values
  - File padding functionality
  - Error handling for various edge cases
  - Data preservation tests
  - Pathlib functionality tests

- **`test_lpcvtcksum_integration.py`** - Integration tests for script execution
  - Script existence and shebang validation
  - Command-line argument handling
  - Overall script behavior tests

- **`run_all_tests.py`** - Standalone test runner
  - Runs all tests with detailed output
  - Provides comprehensive test summary

## Running Tests

### Run All Tests
```bash
# Using the standalone runner
python run_all_tests.py
```

### Run Specific Test Categories
```bash
# Run only unit tests
python test_lpcvtcksum_unit.py

# Run only integration tests
python test_lpcvtcksum_integration.py
```

### Run Individual Test Methods
```bash
# Run a specific test method
python -m unittest test_lpcvtcksum_unit.TestLpcVtcksum.test_checksum_calculation_simple

# Run all tests in a specific class
python -m unittest test_lpcvtcksum_unit.TestLpcVtcksum
```

## Test Features

- **Pathlib Integration**: All file operations use `pathlib.Path` for cross-platform compatibility
- **Comprehensive Coverage**: Tests cover checksum calculation, file I/O, error handling, and edge cases
- **Detailed Output**: Test runners provide detailed failure information and success rates
- **Modular Design**: Tests are split by functionality for easier maintenance and development

## Requirements

- Python 3.6+
- `unittest` module (standard library)
- Access to the `lpcvtcksum` script in `../scripts/`

## Test Data

The tests create temporary binary files with ARM vector tables and verify that:
- Checksums are calculated correctly according to the LPC specification
- Files are padded to 4096-byte boundaries
- Additional data beyond the vector table is preserved
- Error conditions are handled gracefully
