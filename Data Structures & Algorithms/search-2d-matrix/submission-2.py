class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        ROWS=len(matrix)
        COLUMNS=len(matrix[0])
        row_present_in=-1
        for i in range(ROWS):
            if matrix[i][0]<=target<=matrix[i][COLUMNS-1]:
                row_present_in=i
                break 
        
        if row_present_in==-1:
            return False
        
        l=0
        r=COLUMNS-1 
        while l<=r:
            m=(l+r)//2
            if matrix[row_present_in][m]==target:
                return True
            elif matrix[row_present_in][m]>target:
                r=m-1
            else:
                l=m+1

        return False
        '''
        ROWS=len(matrix)
        COLUMNS=len(matrix[0])

        l=0
        r=ROWS*COLUMNS-1 
        while l<=r:
            m=(l+r)//2 
            row=m//COLUMNS 
            col=m%COLUMNS 
            if target == matrix[row][col]:
                return True
            elif target>matrix[row][col]:
                l=m+1
            else:
                r=m-1
        return False 