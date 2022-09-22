class Solution:
    def findCombination(self,ind, arr,target, ans, ds):
        if ind== len(arr):
            if target==0:
                ans.append(ds.copy())
            return
        
        if arr[ind] <= target:
            ds.append(arr[ind])
            self.findCombination(ind, arr,target-arr[ind], ans, ds)
            ds.pop()
        self.findCombination(ind+1, arr,target, ans, ds)
        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans =[]
        ds=[]
        self.findCombination(0,candidates,target, ans, ds)
        return ans