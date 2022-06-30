'''
Problem - https://leetcode.com/problems/3sum
Solution - https://www.youtube.com/watch?v=onLoX6Nhvmg

Explaination -
    1. We used two pointer approach in this probelm , the same approach we used in this problem -
        https://leetcode.com/problems/two-sum-ii-input-array-is-sorted (day3_two_sum). 
    2. For this we need to sort the array first and then loop it once over the array.
    3. we have to achive this condition a+b+c = 0 for this we modify the equation to
        a = -(b+c)
    4. b and c will be fetched from two pointer approach
    5. append all the 3 values a,b,c in to result array
    6. TC - O(N*N), SC - O(M) m is number of triplets , Auxillary space is O(1) bcz result is used to store the ans which we have to return.
'''

def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort() #sorting because two pointer approach will work if array is sorted
    n = len(nums)
    for i in range(0,n-2):#looping over 3rd last element as we have to form triplets 
        if i == 0 or (i > 0 and nums[i]!=nums[i-1]):#to avoid the duplicates for a(first element)
            target = 0 - nums[i]
            low = i + 1#we will search for target from the range low to high
            high = n - 1
            while (low < high ):
                if nums[low] + nums[high] == target:
                    ans=[nums[i],nums[low],nums[high]]
                    res.append(ans)
                    while low <high and nums[low+1] == nums[low]:# to avoid duplicates
                        low = low +1
                    while low <high and nums[high-1] == nums[high]: # to avoid duplicates
                        high= high - 1
                    low = low + 1 #this will make sure our low pointer is not at duplicate element
                    high =high - 1 #this will make sure our high pointer is not at duplicate element
                elif nums[low] + nums[high] < target:
                    low = low + 1
                else:
                    high = high - 1
    return res  