class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS=len(board),len(board[0])
        #use hash set to prevent checking same square 
        visited=set()
        def dfs(r,c,i):
            #out of bounds 
            if r>=ROWS or c>=COLS or r<0 or c<0:
                return False
            #desirable char not present 
            if board[r][c]!=word[i]:
                return False
            #already visited 
            if (r,c) in visited:
                return False 
            if i==len(word)-1:
                return True
        
            #desirable char present, hence add to visited + try in all 4 directions
            visited.add((r,c))
            res=dfs(r-1,c,i+1) or dfs(r,c-1,i+1) or dfs(r+1,c,i+1) or dfs(r,c+1,i+1)
            visited.remove((r,c))
            return res 

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True  
            
        return False 