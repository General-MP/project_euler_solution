def sum_of_multiples_below(limit: int, divisor: int) -> int:
    """Return the sum of all multiples of 'divisor' below 'limit'.

    Preconditions:
        - limit > 0
        - divisor > 0

    Args:
        limit (int): The upper limit (exclusive).
        divisor (int): The divisor for which to find multiples.

    Returns:
        int: The sum of all multiples of 'divisor' below 'limit'.

    >>> sum_of_multiples_below(10, 3)
    18  # (3 + 6 + 9)

    >>> sum_of_multiples_below(10, 5)
    5  # (5)
    """
    n = (limit - 1) // divisor  # Number of terms
    return divisor * n * (n + 1) // 2  # Sum of arithmetic sequence


def calculate_sum_of_multiples(limit: int) -> int:
    """Calculate the sum of all natural numbers below 'limit' divisible by 3 or 5.

    Preconditions:
        - limit > 0

    Args:
        limit (int): The upper limit (exclusive).

    Returns:
        int: The sum of all numbers divisible by 3 or 5 below 'limit'.

    >>> calculate_sum_of_multiples(10)
    23  # (3 + 5 + 6 + 9)
    """
    sum_3 = sum_of_multiples_below(limit, 3)
    sum_5 = sum_of_multiples_below(limit, 5)
    sum_15 = sum_of_multiples_below(limit, 15)  # Avoid double-counting

    return sum_3 + sum_5 - sum_15


def main() -> None:
    """Main function to execute the program logic."""
    LIMIT = 1000  # Upper limit for the calculation
    result = calculate_sum_of_multiples(LIMIT)
    print(f"The sum of all natural numbers below {LIMIT} that are multiples of 3 or 5 is: {result}")


if __name__ == "__main__":
    main()