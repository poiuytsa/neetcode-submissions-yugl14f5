class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS=len(grid),len(grid[0])
        dirs=((1,0),(-1,0),(0,1),(0,-1))

        def bfs(r,c):
            dist=0
            q=deque([(r,c)])
            visited={(r,c)}
            while q:
                for i in range(len(q)):
                    r,c=q.popleft()
                    if grid[r][c]==0:
                        return dist 
                    for dr,dc in dirs:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited and grid[nr][nc]!=-1:
                            visited.add((nr,nc))
                            q.append((nr,nc))
                dist+=1
            return 2147483647

            


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]!= 0 and grid[i][j]!= -1:
                    grid[i][j]=bfs(i,j)
