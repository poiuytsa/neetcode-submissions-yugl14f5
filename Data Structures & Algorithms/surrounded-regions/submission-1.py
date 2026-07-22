class Solution:
    def solve(self, board: List[List[str]]) -> None:
        notSurr=set()
        ROWS,COLS=len(board),len(board[0])
        dirs=((1,0),(-1,0),(0,1),(0,-1))

        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or board[r][c]!="O" or (r,c) in notSurr:
                return
            notSurr.add((r,c))
            for dr,dc in dirs:
                dfs(r+dr,c+dc)

        for j in range(COLS):
            dfs(0,j)
            dfs(ROWS-1,j)
        
        for i in range(ROWS):
            dfs(i,0)
            dfs(i,COLS-1)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="O" and (i,j) not in notSurr:
                    board[i][j]="X"