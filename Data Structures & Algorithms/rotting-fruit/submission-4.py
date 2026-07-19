class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        dirs=((1,0),(-1,0),(0,1),(0,-1))
        q=deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    q.append((i,j))
        time=0    
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()

                for dr,dc in dirs:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==1:
                        q.append((nr,nc))
                        grid[nr][nc]=2
            if q:
                time+=1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    return -1

        return time