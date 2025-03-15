import copy
class Solution:
    def dfs(self,row,col,image,initialColor,newColor,dRow,dCol,ans):
        ans[row][col] = newColor

        n = len(image)
        m = len(image[0])

        for i in range(4):
            nRow = row + dRow[i]
            nCol = col + dCol[i]
            if nRow >= 0 and nRow < n and nCol >= 0 and nCol < m and ans[nRow][nCol]!= newColor and image[nRow][nCol] == initialColor:
                self.dfs(nRow,nCol,image,initialColor,newColor,dRow,dCol,ans)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ans = copy.deepcopy(image)
        initialColor = image[sr][sc]
        newColor = color
        # delta row and del col values
        dRow = [-1,0,+1,0]
        dCol = [0,-1,0,+1]

        self.dfs(sr,sc,image,initialColor,newColor,dRow,dCol,ans)
        return ans