class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        col, row = m-1, 0
        while col>=0 and row < n:
            num= matrix[row][col]
            if num > target:
                col = col - 1
            elif num < target:
                row =row + 1
            elif num == target:
                return True
        return False
                
                
       