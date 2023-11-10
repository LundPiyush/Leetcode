class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) #row
        n = len(matrix[0]) #column
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False