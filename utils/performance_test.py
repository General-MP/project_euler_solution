import time
import memory_profiler
from typing import Callable, Any, Dict, Tuple
from rich.console import Console
from rich.table import Table


def measure_performance(func: Callable, *args: Any, **kwargs: Any) -> Tuple[float, float, Any]:
    """Measure the execution time and memory usage of a given function.

    Args:
        func (Callable): The function to test.
        *args: Positional arguments for the function.
        **kwargs: Keyword arguments for the function.

    Returns:
        Tuple[float, float, Any]: Execution time (in seconds), memory usage (in MiB), and the function result.
    """
    mem_before = memory_profiler.memory_usage()[0]
    start_time = time.time()

    result = func(*args, **kwargs)

    end_time = time.time()
    mem_after = memory_profiler.memory_usage()[0]

    exec_time = end_time - start_time
    mem_usage = mem_after - mem_before

    return exec_time, mem_usage, result

def display_performance_table(functions: Dict[str, Callable], *args: Any, **kwargs: Any) -> None:
    """Display a performance table using the rich library.

    Args:
        functions (Dict[str, Callable]): A dictionary of function names and their corresponding callables.
        *args: Positional arguments to be passed to all tested functions.
        **kwargs: Keyword arguments to be passed to all tested functions.
    """
    console = Console()
    table = Table(title="Function Performance Comparison")

    # Add columns
    table.add_column("Function", justify="left", style="cyan", no_wrap=True)
    table.add_column("Execution Time (s)", justify="right", style="green")
    table.add_column("Memory Usage (MiB)", justify="right", style="magenta")

    # Measure performance for each function
    for func_name, func in functions.items():
        exec_time, mem_usage, _ = measure_performance(func, *args, **kwargs)
        table.add_row(
            func_name,
            f"{exec_time:.6f}",
            f"{mem_usage:.4f}"
        )

    console.print(table)


if __name__ == "__main__":
    # Example functions
    SUM_UNTIL = 10
    def loop_sum(SUM_UNTIL: int) -> int:
        result = 0
        for i in range(SUM_UNTIL + 1):
            result += i
        return result
    
    def generator_sum(SUM_UNTIL: int) -> int:
        return sum(i for i in range(SUM_UNTIL))
    # Define the functions to test
    functions_to_test = {
        "loop_sum": loop_sum,
        "generator_sum": generator_sum
    }

    # Display the performance table
    display_performance_table(functions_to_test, 1000)
