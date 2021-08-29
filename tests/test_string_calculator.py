import pytest

from calc.string_calculator import add

def test_stringcalculator_must_return_zero_on_empty_string():
    assert add("") == 0