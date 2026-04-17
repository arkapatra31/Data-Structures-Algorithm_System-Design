"""
Recursion → Dynamic Programming: Climbing Stairs
==================================================
The full optimization path in one file:
    Brute-force → Memoization → Tabulation → Space-optimized

Problem: You can climb 1 or 2 steps at a time.
How many distinct ways to reach step n?

This is equivalent to Fibonacci — and the optimization
techniques apply to ALL DP problems.
"""

import time
from functools import lru_cache


# ── Step 1: Brute-Force Recursion — O(2^n) ──────────────────
def climb_recursive(n: int) -> int:
    """
    At each step, branch into two choices: take 1 step or 2 steps.
    Massive redundant computation — same as naive Fibonacci.
    """
    if n <= 1:
        return 1
    return climb_recursive(n - 1) + climb_recursive(n - 2)


# ── Step 2: Memoization (Top-Down DP) — O(n) ────────────────
@lru_cache(maxsize=None)
def climb_memo(n: int) -> int:
    """
    Same logic, but cache results.
    First call to climb_memo(k) computes; subsequent calls are O(1).
    """
    if n <= 1:
        return 1
    return climb_memo(n - 1) + climb_memo(n - 2)


def climb_memo_manual(n: int, memo: dict = None) -> int:
    """Manual dictionary-based memoization."""
    if memo is None:
        memo = {}
    if n <= 1:
        return 1
    if n not in memo:
        memo[n] = climb_memo_manual(n - 1, memo) + climb_memo_manual(n - 2, memo)
    return memo[n]


# ── Step 3: Tabulation (Bottom-Up DP) — O(n) ────────────────
def climb_tabulation(n: int) -> int:
    """
    Build the answer table from base cases upward.
    No recursion overhead, no risk of stack overflow.
    """
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# ── Step 4: Space-Optimized — O(n) time, O(1) space ─────────
def climb_optimized(n: int) -> int:
    """
    We only ever look at the previous two values.
    No need for the full array.
    """
    if n <= 1:
        return 1
    a, b = 1, 1  # dp[0], dp[1]
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ── Extended: k steps at a time ──────────────────────────────
def climb_k_steps(n: int, k: int) -> int:
    """Generalized: can take 1, 2, ..., k steps at a time."""
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(k, i) + 1):
            dp[i] += dp[i - j]
    return dp[n]


# ── Demo & Benchmark ─────────────────────────────────────────
if __name__ == "__main__":
    print("Ways to climb n stairs (1 or 2 steps at a time):")
    for i in range(11):
        print(f"  n={i}: {climb_optimized(i)} ways")

    print("\n--- Benchmark (n=35) ---")
    approaches = [
        ("Brute-force", lambda: climb_recursive(35)),
        ("Memoized", lambda: climb_memo(35)),
        ("Tabulation", lambda: climb_tabulation(35)),
        ("Optimized", lambda: climb_optimized(35)),
    ]

    for name, fn in approaches:
        if name == "Memoized":
            climb_memo.cache_clear()
        start = time.time()
        result = fn()
        elapsed = time.time() - start
        print(f"  {name:12s}: {result:>12,}  ({elapsed:.6f}s)")

    print("\n--- With k=3 steps ---")
    for i in range(11):
        print(f"  n={i}: {climb_k_steps(i, 3)} ways")
