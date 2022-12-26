class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(sr, sc):
            grid[sr][sc] = 0

            nonlocal current
            current += 1    

            if sr > 0 and grid[sr - 1][sc] == 1:
                dfs(sr - 1, sc)
            if sr < leny and grid[sr + 1][sc] == 1:
                dfs(sr + 1, sc)
            if sc > 0 and grid[sr][sc - 1] == 1:
                dfs(sr, sc - 1)
            if sc < lenx and grid[sr][sc + 1] == 1:
                dfs(sr, sc + 1)

            return current

        maximum = 0
        
        leny, lenx = len(grid) - 1, len(grid[0]) - 1
        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                if grid[y][x] == 0: continue
                current = 0
                maximum =  max(maximum, dfs(y, x))

        return maximum
