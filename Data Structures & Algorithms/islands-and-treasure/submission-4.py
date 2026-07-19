class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        #brute force
        
        '''
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
        '''

        # multi source bfs -> 1) find all treasures
        #                     2) multi souce bfs (1 bfs from each treasure, and update the grid)

        ROWS,COLS=len(grid),len(grid[0])
        dirs=((1,0),(-1,0),(0,1),(0,-1))

        visited=set()
        q=deque()
        #step 1 - finding the gates 
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    q.append((i,j))
                    visited.add((i,j))
        
        dist=1
        while q:
            for i in range(len(q)):
                r,c=q.popleft()

                for dr,dc in dirs:
                    nr=dr+r
                    nc=dc+c
                    if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited and grid[nr][nc]!=-1:
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        grid[nr][nc]=dist
            
            dist+=1
