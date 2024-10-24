from euler_001_multiples_of_3_or_5.solutions.mathematical_solution_001 import (
    sum_of_multiples_below, calculate_sum_of_multiples
)
from euler_001_multiples_of_3_or_5.solutions.pythonic_solution_001 import (
    sum_of_multiples_of_3_or_5_below
)
from euler_001_multiples_of_3_or_5.solutions.imperative_solution_001 import (
    sum_of_multiples_of_3_or_5_below
)

# Mathematical Solution Tests
def test_sum_of_multiples_basic() -> None:
    """Test the mathematical solution with basic cases."""
    assert calculate_sum_of_multiples(10) == 23  # 3 + 5 + 6 + 9

def test_sum_of_multiples_prime_limit() -> None:
    """Test the mathematical solution with a prime number as limit."""
    assert calculate_sum_of_multiples(7) == 14  # 3 + 5

def test_sum_of_multiples_no_valid_multiples() -> None:
    """Test the mathematical solution with a limit without any valid multiples."""
    assert calculate_sum_of_multiples(2) == 0  # No multiples

def test_sum_of_multiples_large_limit() -> None:
    """Test the mathematical solution with a large limit to ensure performance."""
    assert calculate_sum_of_multiples(10_000) > 0  # Large input

# Pythonic Solution Tests
def test_pythonic_solution_basic() -> None:
    """Test the Pythonic solution with basic cases."""
    assert sum_of_multiples_of_3_or_5_below(10) == 23

def test_pythonic_solution_prime_limit() -> None:
    """Test the Pythonic solution with a prime number as limit."""
    assert sum_of_multiples_of_3_or_5_below(7) == 14

def test_pythonic_solution_no_valid_multiples() -> None:
    """Test the Pythonic solution with no valid multiples."""
    assert sum_of_multiples_of_3_or_5_below(2) == 0

# Imperative Solution Tests
def test_imperative_solution_basic() -> None:
    """Test the imperative solution with basic cases."""
    assert sum_of_multiples_of_3_or_5_below(10) == 23

def test_imperative_solution_large_limit() -> None:
    """Test the imperative solution with a large input to ensure performance."""
    assert sum_of_multiples_of_3_or_5_below(10_000) > 0

if __name__ == "__main__":
    import pytest
    pytest.main(args=['-v'])
