"""
Recursion Basics: Fibonacci
============================
The classic example of overlapping subproblems.
Shows the optimization path: recursion → memoization → tabulation.

fib(0)=0, fib(1)=1, fib(n) = fib(n-1) + fib(n-2)
"""

import time
from functools import lru_cache


# ── 1. Naive Recursion — O(2^n) ──────────────────────────────
def fib_naive(n: int) -> int:
    """Exponential time — recomputes everything."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# ── 2. Memoization (Top-Down DP) — O(n) ─────────────────────
@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    """Each subproblem solved once, cached automatically."""
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_memo_manual(n: int, cache: dict = None) -> int:
    """Manual memoization with a dictionary."""
    if cache is None:
        cache = {}
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fib_memo_manual(n - 1, cache) + fib_memo_manual(n - 2, cache)
    return cache[n]


# ── 3. Tabulation (Bottom-Up DP) — O(n) ─────────────────────
def fib_tabulation(n: int) -> int:
    """Iterative, fills table from base cases up."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# ── 4. Space-Optimized — O(n) time, O(1) space ──────────────
def fib_optimized(n: int) -> int:
    """Only need previous two values at any point."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ── Demo & Benchmark ─────────────────────────────────────────
if __name__ == "__main__":
    print("First 15 Fibonacci numbers:")
    print([fib_optimized(i) for i in range(15)])

    # Benchmark naive vs optimized for n=35
    print("\n--- Performance Comparison (n=35) ---")

    start = time.time()
    result = fib_naive(35)
    naive_time = time.time() - start
    print(f"Naive:      fib(35) = {result}  ({naive_time:.4f}s)")

    start = time.time()
    fib_memo.cache_clear()
    result = fib_memo(35)
    memo_time = time.time() - start
    print(f"Memoized:   fib(35) = {result}  ({memo_time:.6f}s)")

    start = time.time()
    result = fib_tabulation(35)
    tab_time = time.time() - start
    print(f"Tabulation: fib(35) = {result}  ({tab_time:.6f}s)")

    start = time.time()
    result = fib_optimized(35)
    opt_time = time.time() - start
    print(f"Optimized:  fib(35) = {result}  ({opt_time:.6f}s)")

    print(f"\nNaive is ~{naive_time / max(memo_time, 1e-9):.0f}x slower than memoized!")
