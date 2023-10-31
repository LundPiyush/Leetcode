class Solution:
    def generate_row(self,row):
        ans = 1
        ans_row =[1]
        
        for i in range(1,row):
            ans = ans * (row-i)
            ans = ans // i
            ans_row.append(ans)
        return ans_row     

    def generate(self, numRows: int) -> List[List[int]]:
        ans =[]
        for i in range(1,numRows+1):
            ans.append(self.generate_row(i))
            
        return ans