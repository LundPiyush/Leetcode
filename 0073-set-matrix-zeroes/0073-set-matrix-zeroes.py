class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m= len(matrix[0])
        
        row=n*[0]
        col=m*[0]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i]=1
                    col[j]=1
        
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0
                    
        print(matrix)
                    
        