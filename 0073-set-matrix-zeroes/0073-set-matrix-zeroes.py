class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Optimal approach 
        '''
        Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns 
        Reason: In this approach, we are also traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

Space Complexity: O(1) as we are not using any extra space.
        '''
        
        
        n = len(matrix)   
        m= len(matrix[0])  
        col0 = 1
        #row=n*[0]   #row-array ->  matrix[...][0]
        #col=m*[0]   #column-array -> matrix[0][...]
        
        # step 1: Traverse the matrix and
        # mark 1st row & col accordingly
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j!= 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        
        # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]!=0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
                        
        
        #step 3: Finally mark the 1st col & then 1st row:
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0
        
    """
    okayish approach :
    
    Time Complexity: O(2*(N*M)), where N = no. of rows, M = no. of columns.
    Reason: We are traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.
    
    Space Complexity: O(N) + O(M) 
    Reason: O(N) is for using the row array and O(M) is for using the col array.

        n = len(matrix)   
        m= len(matrix[0])  
        
        row=n*[0]   #row-array
        col=m*[0]   #column-array
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i]=1
                    col[j]=1
        
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0
                    
        """
        
            
        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        