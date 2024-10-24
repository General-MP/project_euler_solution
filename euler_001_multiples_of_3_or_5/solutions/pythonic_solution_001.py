def sum_of_multiples_of_3_or_5_below(limit: int) -> int:
    """Calculate the sum of all natural numbers below 'limit' divisible by 3 or 5.

    This function uses a generator expression and the built-in sum() function 
    to efficiently calculate the sum. The entire range is traversed once.

    Time Complexity:
        - O(n): Linear time, as the function iterates over the range.

    Memory Complexity:
        - O(1): Constant space, as the generator expression is used 
          (no intermediate list stored in memory).

    Args:
        limit (int): The upper limit (exclusive).

    Returns:
        int: The sum of all multiples of 3 or 5 below 'limit'.

    >>> generator_expression_solution(10)
    23  # (3 + 5 + 6 + 9)
    """
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)

def main() -> None:
    """Main function to execute the program logic."""
    LIMIT = 1000  # Upper limit for the calculation
    result = sum_of_multiples_of_3_or_5_below(LIMIT)
    print(result)

if __name__ == '__main__':
    main()