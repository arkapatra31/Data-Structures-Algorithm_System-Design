"""
Recursion Basics: Factorial
===========================
The simplest recursive example. n! = n × (n-1) × ... × 1

Time Complexity:  O(n)
Space Complexity: O(n) — due to call stack depth
"""


def factorial(n: int) -> int:
    """Calculate n! recursively."""
    # Base case: 0! = 1! = 1
    if n <= 1:
        return 1
    # Recursive case: n! = n × (n-1)!
    return n * factorial(n - 1)


def factorial_tail(n: int, accumulator: int = 1) -> int:
    """
    Tail-recursive version of factorial.
    Note: Python does NOT optimize tail calls, but this pattern
    is useful to understand before converting to iteration.
    """
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)


def factorial_iterative(n: int) -> int:
    """Iterative version — avoids stack overflow for large n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ── Demo ──────────────────────────────────────────────────────
if __name__ == "__main__":
    for i in range(11):
        print(f"factorial({i}) = {factorial(i)}")

    print("\n--- Comparing all three approaches ---")
    n = 20
    print(f"Recursive:      factorial({n}) = {factorial(n)}")
    print(f"Tail-recursive: factorial({n}) = {factorial_tail(n)}")
    print(f"Iterative:      factorial({n}) = {factorial_iterative(n)}")
