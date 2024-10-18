"""
Test module for the get_gcd_multiplier function from the calculations module.

This module contains unit tests for the get_gcd_multiplier function, which
calculates the multiplier. The tests are designed to validate the correctness
of the function across various input scenarios.

Imported modules:
- os: A module for importing father files.
- pytest: A framework for writing and running tests.
- sys: A module for manipulating Python's runtime environment.

Constants:
- CALCULATIONS_PACKAGE_PATH (str): A relative path to the calculations
  package directory, used to import modules for testing.

Functions:
- test_get_gcd_multiplier(a_number: int, b_number: int, result: int) ->
  None: Run tests for get_gcd_multiplier function.

Usage:
  pytest test_get_gcd_multiplier.py

Parameters:
- a_number (int): The first integer input for the GCD calculation.
- b_number (int): The second integer input for the GCD calculation.
- result (int): The expected output from the get_gcd_multiplier
  function for the given inputs a_number and b_number.

Test Cases:
- (1, 1) should return 1
- (999, 3) should return 332
- (1071, 462) should return 2
- (1337, 228) should return 5
- (123654789, 7) should return 17664969
"""

import os

import pytest

from sys import path

path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data import CALCULATIONS_PACKAGE_PATH

path.append(CALCULATIONS_PACKAGE_PATH)

from calculations.functions import get_gcd_multiplier


@pytest.mark.parametrize(
    "a_number, b_number, result",
    [
        (1, 1, 1),
        (999, 3, 332),
        (1071, 462, 2),
        (1337, 228, 5),
        (123654789, 7, 17664969),
    ],
)
def test_get_gcd_multiplier(a_number: int, b_number: int, result: int) -> None:
    """
    Test the get_gcd_multiplier function for correctness.

    This function asserts that the output of get_gcd_multiplier
    for  given inputs a_number and b_number matches the expected result.

    Parameters:
    - a_number (int): The first integer input for the GCD calculation.
    - b_number (int): The second integer input for the GCD calculation.
    - result (int): The expected output from the get_gcd_multiplier
      function for the given inputs.

    Raises:
    AssertionError: If the actual output from get_gcd_multiplier
                    does not equal the expected result.
    """

    assert get_gcd_multiplier(a_number, b_number) == result
