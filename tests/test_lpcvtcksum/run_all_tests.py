#!/usr/bin/env python3
"""
Combined test runner for lpcvtcksum test suite.

This script runs both unit tests and integration tests for the lpcvtcksum script.
"""

from sys import exit
from unittest import TestSuite, TestLoader, TextTestRunner
from pathlib import Path

# Import test classes
from test_lpcvtcksum_unit import TestLpcVtcksum
from test_lpcvtcksum_integration import TestLpcVtcksumIntegration

def run_all_tests():
    """Run all tests with detailed output."""
    # Create test suite
    test_suite = TestSuite()
    
    # Add all test methods
    for test_class in [TestLpcVtcksum, TestLpcVtcksumIntegration]:
        tests = TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests with detailed output
    runner = TextTestRunner(verbosity=2, buffer=True)
    result = runner.run(test_suite)
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"Test Summary:")
    print(f"  Tests run: {result.testsRun}")
    print(f"  Failures: {len(result.failures)}")
    print(f"  Errors: {len(result.errors)}")
    print(f"  Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\nFailures:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback.split(chr(10))[-2]}")
    
    if result.errors:
        print(f"\nErrors:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback.split(chr(10))[-2]}")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_all_tests()
    exit(0 if success else 1)
