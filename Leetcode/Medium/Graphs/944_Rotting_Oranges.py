"""
994 — Rotting Oranges
=====================
Given a grid of 0 (empty), 1 (fresh orange), 2 (rotten orange),
every minute any fresh orange adjacent (4-directionally) to a rotten
orange also becomes rotten.
Return the minimum minutes until all fresh oranges rot, or -1 if impossible.

Approach: Multi-source BFS — seed the queue with every initially rotten
orange simultaneously and expand level by level (1 level = 1 minute).
Time: O(M × N)  |  Space: O(M × N)
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi-source BFS from all initially rotten oranges.

        Args:
            grid: 2D list — 0 = empty, 1 = fresh orange, 2 = rotten orange

        Returns:
            int — minimum minutes for all oranges to rot, or -1 if impossible
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Seed the queue with every rotten orange at minute 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))   # (row, col, minute)
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Early exit — nothing left to rot
        if fresh_count == 0:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up
        minutes_elapsed = 0

        while queue:
            row, col, minute = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2              # mark as rotten in-place
                    fresh_count -= 1
                    minutes_elapsed = minute + 1
                    queue.append((nr, nc, minute + 1))  # add to back of queue

        return minutes_elapsed if fresh_count == 0 else -1


# ── Demo ──
if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(Solution().orangesRotting(grid))  # Output: 4
