class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        #bottom up
        dp=[[0]*(COLS+1) for _ in range(ROWS+1)]
        res=0
        for i in range(ROWS-1,-1,-1):
            for j in range(COLS-1,-1,-1):
                #cuz if its 0, its 0 anways
                if matrix[i][j]=="1":
                    dp[i][j]=1+min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1])
                    res=max(res,dp[i][j])
        
        return res**2 
