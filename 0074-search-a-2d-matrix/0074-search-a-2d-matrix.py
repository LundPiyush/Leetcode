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

        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m - 1]:
                return self.binarySearch(matrix[i], target)
        return False