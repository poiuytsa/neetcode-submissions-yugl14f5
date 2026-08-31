class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        memo = [[None] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return grid[r][c]

            if memo[r][c] is not None:
                return memo[r][c]

            down = dfs(r + 1, c) if r + 1 < ROWS else float('inf')
            right = dfs(r, c + 1) if c + 1 < COLS else float('inf')

            memo[r][c] = grid[r][c] + min(down, right)
            return memo[r][c]

        return dfs(0, 0)
