
from queue import Queue
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for _ in range(n)]

        time,ans = 0,-1
        q = Queue()
        dRow = [-1,0,+1,0]
        dCol = [0,-1,0,+1]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    vis[i][j] = 2
                    q.put(((i,j),time))

        while not q.empty():
            ((row, col), time) = q.get()
            ans = max(ans,time)
            for i in range(4):
                nRow = row + dRow[i]
                nCol = col + dCol[i]

                if nRow >= 0 and nRow < n and nCol >=0 and nCol < m and grid[nRow][nCol]== 1 and vis[nRow][nCol] != 2:
                    vis[nRow][nCol] = 2
                    q.put(((nRow, nCol), time+1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] != 2:
                    return -1
        return ans