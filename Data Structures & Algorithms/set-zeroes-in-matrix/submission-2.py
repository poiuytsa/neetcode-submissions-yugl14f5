class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS,COLS=len(matrix),len(matrix[0])
        # zeroCols,zeroRows=set(),set()

        # #O(m+n) space
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if not matrix[i][j]:
        #             zeroRows.add(i)
        #             zeroCols.add(j)
                
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if i in zeroRows or j in zeroCols:
        #             matrix[i][j]=0
            
        #O(1) space 

        rowOneZero,columnOneZero=False,False
        #top left, may rep 0th column or 0th row or both
        if matrix[0][0]==0:
            rowOneZero,columnOneZero=True,True
        else:
            for i in range(COLS):
                if matrix[0][i]==0:
                    rowOneZero=True
            for i in range(ROWS):
                if matrix[i][0]==0:
                    columnOneZero=True

        #mark in first row and col
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0

        if rowOneZero:
            for i in range(COLS):
                matrix[0][i]=0
        if columnOneZero:
            for i in range(ROWS):
                matrix[i][0]=0

            