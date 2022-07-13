'''
Problem - https://leetcode.com/problems/maximum-product-subarray
Solution - This is https://www.youtube.com/watch?v=GbJh0MjUa5U
We have to iterate in both directions to decide weather to include first element(if negative) or last element(if negative)

consider exalple -8 5 3 2 1
if we run only one loop like kidane's algorithm we will include get the product in negative

'''

import sys

def maxProduct(self, nums: List[int]) -> int:
    product_so_far=1
    max_product=-sys.maxsize-1
    
    for i in range(0,len(nums)):
        product_so_far *= nums[i]
        max_product = max(max_product,product_so_far)
        if nums[i] == 0:
            product_so_far = 1
    product_so_far=1
    for i in range(len(nums)-1,-1,-1):
        product_so_far =product_so_far*nums[i]
        max_product = max(max_product, product_so_far)
        if nums[i] == 0:
            product_so_far = 1  
    return max_product
