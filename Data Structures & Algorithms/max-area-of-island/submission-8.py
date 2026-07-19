class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        self.res,self.currArea=0,0
        directions=((1,0),(-1,0),(0,1), (0,-1))

        def dfs(i,j):
            if i<0 or j<0 or i>=ROWS or j>=COLS or not grid[i][j]:
                return 
            grid[i][j]=0
            self.currArea+=1
            for dr,dc in directions:
                dfs(i+dr,j+dc)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    #self.currArea=1
                    dfs(i,j)
                    self.res=max(self.res,self.currArea)
                    self.currArea=0

        
        return self.res
