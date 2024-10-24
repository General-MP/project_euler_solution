from hypothesis import given, strategies as st
from euler_001_multiples_of_3_or_5.solutions.mathematical_solution_001 import (
    sum_of_multiples_below, calculate_sum_of_multiples
)
from euler_001_multiples_of_3_or_5.solutions.pythonic_solution_001 import (
    sum_of_multiples_of_3_or_5_below
)
from euler_001_multiples_of_3_or_5.solutions.imperative_solution_001 import (
    sum_of_multiples_of_3_or_5_below
)

@given(st.integers(min_value=1, max_value=10_000), st.integers(min_value=1, max_value=100))
def test_sum_of_multiples_below_random_inputs(limit: int, divisor: int) -> None:
    """Property-based test for sum_of_multiples_below with random inputs."""
    result = sum_of_multiples_below(limit, divisor)
    assert result >= 0  # Ensure non-negative result

@given(st.integers(min_value=1, max_value=10_000))
def test_calculate_sum_of_multiples_random_inputs(limit: int) -> None:
    """Property-based test for calculate_sum_of_multiples with random inputs."""
    result = calculate_sum_of_multiples(limit)
    assert result >= 0

@given(st.integers(min_value=1, max_value=10_000))
def test_pythonic_solution_random_inputs(limit: int) -> None:
    """Property-based test for Pythonic solution with random inputs."""
    result = sum_of_multiples_of_3_or_5_below(limit)
    assert result >= 0

@given(st.integers(min_value=1, max_value=10_000))
def test_imperative_solution_random_inputs(limit: int) -> None:
    """Property-based test for imperative solution with random inputs."""
    result = sum_of_multiples_of_3_or_5_below(limit)
    assert result >= 0

if __name__ == "__main__":
    import pytest
    pytest.main(args=['-v'])
