class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroCols,zeroRows=set(),set()
        ROWS,COLS=len(matrix),len(matrix[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                if not matrix[i][j]:
                    zeroRows.add(i)
                    zeroCols.add(j)
                
        for i in range(ROWS):
            for j in range(COLS):
                if i in zeroRows or j in zeroCols:
                    matrix[i][j]=0
            
        