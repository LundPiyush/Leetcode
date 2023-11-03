/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function(nums) {
    n = nums.length
    mini = Number.MAX_VALUE
    let ans = -1
    for (let i =0;i<n;i++){
        mini = Math.min(mini,nums[i]) 
        if(nums[i]>mini)
            ans = Math.max(ans,nums[i]-mini) 
    }
    
    return ans
};