"""
Backtracking: Permutations & Subsets
=====================================
The choose → explore → un-choose pattern.
Backtracking systematically builds candidates and abandons
(backtracks from) those that fail constraints.
"""


# ── 1. Permutations ──────────────────────────────────────────
def permutations(nums: list) -> list:
    """Generate all permutations of nums."""
    result = []

    def backtrack(path: list, remaining: list):
        if not remaining:              # base case: used all numbers
            result.append(path[:])     # save a COPY of path
            return

        for i in range(len(remaining)):
            path.append(remaining[i])              # choose
            backtrack(path,
                      remaining[:i] + remaining[i + 1:])  # explore
            path.pop()                              # un-choose

    backtrack([], nums)
    return result


# ── 2. Subsets (Power Set) ───────────────────────────────────
def subsets(nums: list) -> list:
    """Generate all subsets. At each element: include or exclude."""
    result = []

    def backtrack(index: int, current: list):
        if index == len(nums):
            result.append(current[:])
            return

        # Branch 1: include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()                  # un-choose

        # Branch 2: exclude nums[index]
        backtrack(index + 1, current)

    backtrack(0, [])
    return result


# ── 3. Combination Sum ──────────────────────────────────────
def combination_sum(candidates: list, target: int) -> list:
    """
    Find all unique combinations that sum to target.
    Each number can be used unlimited times.
    """
    result = []
    candidates.sort()

    def backtrack(start: int, remaining: int, combo: list):
        if remaining == 0:
            result.append(combo[:])
            return
        if remaining < 0:
            return                    # prune: overshot

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break                 # prune: sorted, so all after are too big
            combo.append(candidates[i])
            backtrack(i, remaining - candidates[i], combo)  # i, not i+1 (reuse)
            combo.pop()

    backtrack(0, target, [])
    return result


# ── 4. Letter Combinations of a Phone Number ────────────────
def letter_combinations(digits: str) -> list:
    """Generate all letter combos for phone digits (like T9)."""
    if not digits:
        return []

    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    result = []

    def backtrack(index: int, current: list):
        if index == len(digits):
            result.append("".join(current))
            return

        for letter in phone_map[digits[index]]:
            current.append(letter)
            backtrack(index + 1, current)
            current.pop()

    backtrack(0, [])
    return result


# ── Demo ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Permutations of [1, 2, 3] ===")
    for p in permutations([1, 2, 3]):
        print(f"  {p}")

    print(f"\n=== Subsets of [1, 2, 3] ===")
    for s in subsets([1, 2, 3]):
        print(f"  {s}")

    print(f"\n=== Combination Sum: target=7, candidates=[2,3,6,7] ===")
    for c in combination_sum([2, 3, 6, 7], 7):
        print(f"  {c}")

    print(f'\n=== Letter Combos of "23" ===')
    print(f"  {letter_combinations('23')}")
