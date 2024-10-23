from solution_001_multiples_of_3_or_5_approach_1 import sum_of_multiples_below, calculate_sum_of_multiples

def test_sum_of_multiples_below() -> None:
    """Unit test for the sum_of_multiples_below function."""
    assert sum_of_multiples_below(10, 3) == 18  # 3 + 6 + 9
    assert sum_of_multiples_below(10, 5) == 5   # 5
    assert sum_of_multiples_below(1000, 15) == 33165

def test_calculate_sum_of_multiples() -> None:
    """Unit test for the calculate_sum_of_multiples function."""
    assert calculate_sum_of_multiples(10) == 23  # 3 + 5 + 6 + 9
    assert calculate_sum_of_multiples(1000) == 233168

if __name__ == "__main__":
    import pytest
    pytest.main(args=['-v'])
