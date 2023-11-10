class Solution:
    def binarySearch(self,nums, target):
        n = len(nums) # size of the array
        low, high = 0, n - 1

        # Perform the steps:
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return False     
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low, high = 0, (n*m) - 1
        
        # Perform the steps:
        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                low = mid + 1
            else:
                high = mid - 1
        return False 