def arithmetic_sequence_solution(limit: int) -> int:
    """Calculate the sum of all natural numbers below 'limit' divisible by 3 or 5.

    This function uses the arithmetic sequence formula to calculate the result 
    in constant time, avoiding loops or iteration.

    Time Complexity:
        - O(1): Constant time, as it uses arithmetic formulas.

    Memory Complexity:
        - O(1): Constant space usage, only a few variables are used.

    Args:
        limit (int): The upper limit (exclusive).

    Returns:
        int: The sum of all multiples of 3 or 5 below 'limit'.

    >>> arithmetic_sequence_solution(10)
    23  # (3 + 5 + 6 + 9)
    """
    n3 = (limit - 1) // 3
    n5 = (limit - 1) // 5
    n15 = (limit - 1) // 15
    return 3 * n3 * (n3 + 1) // 2 + 5 * n5 * (n5 + 1) // 2 - 15 * n15 * (n15 + 1) // 2


def generator_expression_solution(limit: int) -> int:
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


def loop_based_solution(limit: int) -> int:
    """Calculate the sum of all natural numbers below 'limit' divisible by 3 or 5.

    This function uses a for-loop to calculate the sum. It iterates over all 
    numbers below the limit and checks if they are divisible by 3 or 5.

    Time Complexity:
        - O(n): Linear time, as the function iterates through the range.

    Memory Complexity:
        - O(1): Constant space, as only a few variables are used.

    Args:
        limit (int): The upper limit (exclusive).

    Returns:
        int: The sum of all multiples of 3 or 5 below 'limit'.

    >>> loop_based_solution(10)
    23  # (3 + 5 + 6 + 9)
    """
    total_sum = 0
    for n in range(limit):
        if n % 3 == 0 or n % 5 == 0:
            total_sum += n
    return total_sum


def main() -> None:
    """Main function to execute the program logic and display performance."""
    LIMIT = 1000

    # Call the arithmetic sequence solution
    result = arithmetic_sequence_solution(LIMIT)
    print(f"Arithmetic Sequence Solution: {result}")

    # Call the generator expression solution
    result = generator_expression_solution(LIMIT)
    print(f"Generator Expression Solution: {result}")

    # Call the loop-based solution
    result = loop_based_solution(LIMIT)
    print(f"Loop-Based Solution: {result}")


if __name__ == "__main__":
    main()
