/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxi = Number.MIN_SAFE_INTEGER;
    let sum = 0
    const n = nums.length
    for (let i =0;i<n;i++){
        sum = sum + nums[i]
        
        if(sum > maxi) maxi = sum
        
        if(sum <0) sum = 0
        
    }
    return maxi
};