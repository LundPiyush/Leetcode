'''
Problem - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
Solution - https://www.youtube.com/watch?v=TZbo8gzbfzY
'''

'''
Explaination - 
    We use 2 pointer approach . First Hint we get is array is in increasing order
    if summation of both elements is more than expected we know to make the summation closer to our target 
    we have to lower the value of upper limit and vice versa.
'''
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    first_ptr,last_ptr = 0,len(numbers)-1 
    ans = []
    
    while first_ptr < last_ptr :
        if numbers[first_ptr] + numbers[last_ptr] > target:
            last_ptr = last_ptr - 1 
        elif numbers[first_ptr] + numbers[last_ptr] < target:
            first_ptr = first_ptr + 1
        else:
            ans.append(first_ptr + 1)
            ans.append(last_ptr + 1)
            break
    return ans
