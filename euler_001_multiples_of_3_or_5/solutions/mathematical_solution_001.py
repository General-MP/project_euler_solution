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
    # Calculate the number of terms (n) in the sequence of multiples.
    # We subtract 1 from 'limit' because we are only interested in numbers below 'limit'.
    # The '//' operator performs integer division to get the largest integer less than or equal to the quotient.
    n = (limit - 1) // divisor

    # Calculate the sum of the arithmetic sequence using the formula:
    # sum = divisor * n * (n + 1) // 2
    # This formula calculates the sum of the first 'n' multiples of 'divisor'.
    # We use integer division '//' to ensure the result is an integer.
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
    # Apply the inclusion-exclusion principle:
    # Avoid double-counting
    sum_15 = sum_of_multiples_below(limit, 15)  

    return sum_3 + sum_5 - sum_15


def main() -> None:
    """Main function to execute the program logic."""
    LIMIT = 1000  # Upper limit for the calculation
    result = calculate_sum_of_multiples(LIMIT)
    print(f"The sum of all natural numbers below {LIMIT} that are multiples of 3 or 5 is: {result}")


if __name__ == "__main__":
    main()