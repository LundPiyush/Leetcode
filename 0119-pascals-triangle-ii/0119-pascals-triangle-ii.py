class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = 1
        row =[1]
        
        for i in range(1,rowIndex+1):
            ans = ans * (rowIndex+1-i)
            ans = ans // i
            row.append(ans)
        
        
        return row