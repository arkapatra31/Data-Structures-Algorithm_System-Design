"""
Backtracking: N-Queens
=======================
Place N queens on an N×N chessboard so no two attack each other.
Classic constraint-satisfaction problem solved with backtracking.

Time Complexity:  O(N!) — with pruning, much better in practice
Space Complexity: O(N²) for the board, O(N) for tracking sets
"""


def solve_n_queens(n: int) -> list:
    """
    Returns all valid N-Queens solutions.
    Each solution is a list of strings representing the board.
    """
    results = []

    def backtrack(row: int, cols: set, diag1: set, diag2: set, board: list):
        # Base case: placed queens in all rows
        if row == n:
            results.append(["".join(r) for r in board])
            return

        for col in range(n):
            # Check constraints: column, main diagonal, anti-diagonal
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # prune this branch

            # Choose
            board[row][col] = "Q"

            # Explore (add constraints)
            backtrack(
                row + 1,
                cols | {col},
                diag1 | {row - col},
                diag2 | {row + col},
                board,
            )

            # Un-choose
            board[row][col] = "."

    empty_board = [["." for _ in range(n)] for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board)
    return results


def print_board(board: list):
    """Pretty-print a chessboard solution."""
    n = len(board)
    print("  " + " ".join(str(i) for i in range(n)))
    for i, row in enumerate(board):
        cells = " ".join("♛" if c == "Q" else "·" for c in row)
        print(f"{i} {cells}")


# ── Demo ──────────────────────────────────────────────────────
if __name__ == "__main__":
    for n in [4, 5, 6, 8]:
        solutions = solve_n_queens(n)
        print(f"\n{'='*40}")
        print(f"N = {n}: {len(solutions)} solutions found")
        print(f"{'='*40}")

        if n <= 5:
            for i, sol in enumerate(solutions):
                print(f"\n  Solution {i + 1}:")
                print_board(sol)
        else:
            print(f"\n  First solution:")
            print_board(solutions[0])
