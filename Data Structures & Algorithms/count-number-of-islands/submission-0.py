class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        
        def dfs(r, c):
            grid[r][c] = "0"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(R) and nc in range(C) and grid[nr][nc] == "1":
                    dfs(nr, nc)
        
        num = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    num += 1
                    dfs(r, c)
        return num