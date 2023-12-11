/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    
    let count = 0
    let maxi = 0
    
    for (let i = 0;i<nums.length;i++){
        if(nums[i]===1){
            count +=1
            maxi = Math.max(count,maxi) 
        }
        else{
            count = 0
        }
            
    }
    return maxi
    
};