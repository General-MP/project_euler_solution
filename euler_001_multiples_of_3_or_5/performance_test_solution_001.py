from solutions.mathematical_solution_001 import (
    sum_of_multiples_below,
    calculate_sum_of_multiples
)
from solutions.pythonic_solution_001 import sum_of_multiples_of_3_or_5_below
from solutions.imperative_solution_001 import sum_of_multiples_of_3_or_5_below
from utils.performance_test import display_performance_table

def main() -> None:
    """Main function to test the performance of all approaches."""
    LIMIT = 1000  # Upper limit for the calculation

    # Define the functions to test, handling multiple functions for some approaches
    functions_to_test = {
        "Mathematical (calculate_sum_of_multiples)": lambda: calculate_sum_of_multiples(LIMIT),
        "Mathematical (sum_of_multiples_below 3 & 5)": lambda: (
            sum_of_multiples_below(LIMIT, 3) + sum_of_multiples_below(LIMIT, 5)
        ),
        "Pythonic": lambda: sum_of_multiples_of_3_or_5_below(LIMIT),
        "Imperative": lambda: sum_of_multiples_of_3_or_5_below(LIMIT),
    }

    # Display the performance comparison table
    display_performance_table(functions_to_test)

if __name__ == "__main__":
    main()