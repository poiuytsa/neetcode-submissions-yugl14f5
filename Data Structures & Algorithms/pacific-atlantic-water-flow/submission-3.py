class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS=len(heights),len(heights[0])
        dirs=((1,0),(-1,0),(0,1),(0,-1))
        pcf,atl=set(),set()

        def dfs(r,c,visited,prevHeight):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in visited or prevHeight>heights[r][c]:
                return 
            visited.add((r,c))
            for dr,dc in dirs:
                dfs(r+dr,c+dc,visited,heights[r][c])
        
        for j in range(COLS):
            #top row - pacific
            dfs(0,j,pcf,heights[0][j])
            #bottom row - atlantic
            dfs(ROWS-1,j,atl,heights[ROWS-1][j])

        for i in range(ROWS):
            #left column
            dfs(i,0,pcf,heights[i][0])
            #right column
            dfs(i,COLS-1,atl,heights[i][COLS-1])
        

        return list(pcf.intersection(atl))
