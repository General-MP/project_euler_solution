def sum_of_multiples_of_3_or_5_below(limit: int) -> int:
    """Calculate the sum of all natural numbers below 'limit' divisible by 3 or 5.

    This function uses an imperative approach with a for-loop to calculate the sum.
    It iterates over all numbers below the limit and checks if they are divisible by 3 or 5.

    Time Complexity:
        - O(n): Linear time, as the function iterates through the range.

    Memory Complexity:
        - O(1): Constant space, as only a few variables are used.

    Args:
        limit (int): The upper limit (exclusive).

    Returns:
        int: The sum of all multiples of 3 or 5 below 'limit'.

    >>> imperative_solution(10)
    23  # (3 + 5 + 6 + 9)
    """
    total_sum = 0
    for n in range(limit):
        if n % 3 == 0 or n % 5 == 0:
            total_sum += n
    return total_sum

def main() -> None:
    """Main function to execute the program logic."""
    LIMIT = 1000  # Upper limit for the calculation
    print(sum_of_multiples_of_3_or_5_below(LIMIT))

if __name__ == '__main__':
    main()