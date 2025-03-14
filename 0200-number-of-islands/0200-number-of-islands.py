from queue import Queue
from typing import List

class Solution:
    def bfs(self, row, col, vis, grid):
        vis[row][col] = 1
        q = Queue()
        q.put((row, col))
        n, m = len(grid), len(grid[0])
        
        # Only 4 directions (Up, Down, Left, Right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while not q.empty():
            r, c = q.get()

            # traversal to find neigbours
            for drow, dcol in directions: 
                nrow, ncol = r + drow, c + dcol

                if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == '1' and not vis[nrow][ncol]:
                    vis[nrow][ncol] = 1  # Mark as visited
                    q.put((nrow, ncol))

    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        count = 0
        
        for row in range(n):
            for col in range(m):
                if not vis[row][col] and grid[row][col] == '1':
                    count += 1
                    self.bfs(row, col, vis, grid)
        
        return count


