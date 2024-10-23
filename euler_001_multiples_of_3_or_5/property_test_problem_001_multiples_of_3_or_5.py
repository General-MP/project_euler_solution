from hypothesis import given, strategies as st
from solution_001_multiples_of_3_or_5_approach_1 import sum_of_multiples_below, calculate_sum_of_multiples

@given(st.integers(min_value=1, max_value=10_000), st.integers(min_value=1, max_value=100))
def test_sum_of_multiples_below_hypothesis(limit: int, divisor: int) -> None:
    """Property-based test for the sum_of_multiples_below function.

    Verifies that the result is non-negative for valid inputs.
    """
    result = sum_of_multiples_below(limit, divisor)
    assert result >= 0

@given(st.integers(min_value=1, max_value=10_000))
def test_calculate_sum_of_multiples_hypothesis(limit: int) -> None:
    """Property-based test for the calculate_sum_of_multiples function.

    Verifies that the result is non-negative for valid inputs.
    """
    result = calculate_sum_of_multiples(limit)
    assert result >= 0

if __name__ == "__main__":
    import pytest
    pytest.main(args=['-v'])
