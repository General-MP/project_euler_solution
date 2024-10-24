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

def format_value(value: float, unit: str = "") -> str:
    """Format a float value to display it either in scientific notation or with precision."""
    if value < 1e-6:
        return f"{value:.2e} {unit}"
    else:
        return f"{value:.6f} {unit}"

def display_performance_table(functions: Dict[str, Callable], arr: Any) -> None:
    """Display a performance table using the rich library.

    Args:
        functions (Dict[str, Callable]): A dictionary of function names and their corresponding callables.
        arr (Any): The array to be passed as input to all tested functions.
    """
    console = Console()
    table = Table(title="Function Performance Comparison")

    table.add_column("Function", justify="left", style="cyan", no_wrap=True)
    table.add_column("Execution Time (s)", justify="right", style="green")
    table.add_column("Memory Usage (MiB)", justify="right", style="magenta")

    for func_name, func in functions.items():
        exec_time, mem_usage, _ = measure_performance(func, arr)
        table.add_row(
            func_name,
            format_value(exec_time, "s"),
            format_value(mem_usage, "MiB")
        )

    console.print(table)

class BigONotationFunctions:
    """A collection of functions demonstrating different Big-O complexities."""

    @staticmethod
    def _merge(left, right):
        """Helper function for merge sort."""
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        return result + left + right

    @staticmethod
    def Big_O_constant(arr):
        """O(1) - Accesses the first element."""
        return arr[0]

    @staticmethod
    def Big_O_logarithmic(arr):
        """O(log n) - Accesses elements at halving intervals."""
        result = []
        i = len(arr) // 2
        while i > 0:
            result.append(arr[i])
            i //= 2
        return result

    @staticmethod
    def Big_O_linear(arr):
        """O(n) - Sums all elements in the list."""
        total = 0
        for val in arr:
            total += val
        return total

    @staticmethod
    def Big_O_n_log_n(arr):
        """O(n log n) - Sorts the list using merge sort."""
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = BigONotationFunctions.Big_O_n_log_n(arr[:mid])
        right = BigONotationFunctions.Big_O_n_log_n(arr[mid:])
        return BigONotationFunctions._merge(left, right)

    @staticmethod
    def Big_O_quadratic(arr):
        """O(n²) - Returns all pairs of elements."""
        result = []
        for i in arr:
            for j in arr:
                result.append((i, j))
        return result

    @staticmethod
    def Big_O_exponential(arr, max_depth=5):
        """O(2^n) - Generates all subsets with an internal limit."""
        def _subsets(current, index):
            if index == len(arr) or len(current) >= max_depth:
                return [current]
            return (_subsets(current, index + 1) +
                    _subsets(current + [arr[index]], index + 1))
        return _subsets([], 0)

    @staticmethod
    def Big_O_factorial(arr, max_size=4):
        """O(n!) - Generates all permutations with an internal limit."""
        def _permute(l, r):
            if l == r:
                return [arr[:max_size]]
            result = []
            for i in range(l, r + 1):
                arr[l], arr[i] = arr[i], arr[l]
                result.extend(_permute(l + 1, r))
                arr[l], arr[i] = arr[i], arr[l]
            return result
        return _permute(0, min(len(arr) - 1, max_size - 1))

if __name__ == "__main__":
    # Test with different array sizes
    for size in [10, 100, 1000]:
        print(f"\nTesting with array size {size}:")
        arr = list(range(size))

        functions_to_test = {
            "O(1)": BigONotationFunctions.Big_O_constant,
            "O(log n)": BigONotationFunctions.Big_O_logarithmic,
            "O(n)": BigONotationFunctions.Big_O_linear,
            "O(n log n)": BigONotationFunctions.Big_O_n_log_n,
            "O(n²)": BigONotationFunctions.Big_O_quadratic,
            "O(2^n)": BigONotationFunctions.Big_O_exponential,
            "O(n!)": BigONotationFunctions.Big_O_factorial
        }

        display_performance_table(functions_to_test, arr)
