class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # USING 3 pointers 
        i = m-1 # pointing towards last element of arr1
        j = n-1  # pointing towards last element of arr2
        k = m + n - 1  # pointing towards last 0 present in arr1
        
        #looping as long as we have elements in arr2
        while j >= 0:
            # if arr1 has elements and arr1[i]> arr2[j] then pick that ele and put it at kth position
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k]= nums1[i]
                k=k-1
                i=i-1
            else:
                # if arr1[i] <  arr2[j] then pick ele from arr2 and put it at kth position
                nums1[k] = nums2[j]
                k=k-1
                j=j-1
        