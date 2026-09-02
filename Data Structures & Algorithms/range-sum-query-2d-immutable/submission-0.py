class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.ROWS=len(matrix)
        self.COLS=len(matrix[0])
        self.prefixSum=[[-1]*self.COLS for _ in range(self.ROWS)]
        self.suffixSum=[[-1]*self.COLS for _ in range(self.ROWS)]

        for i in range(self.ROWS):
            currSum=0
            for j in range(self.COLS):
                currSum+=self.matrix[i][j]
                self.prefixSum[i][j]=currSum

        for i in range(self.ROWS):
            currSum=0
            for j in range(self.COLS-1,-1,-1):
                currSum+=self.matrix[i][j]
                self.suffixSum[i][j]=currSum
    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res=0
        i=row1
        while i<=row2:
            res+=self.prefixSum[i][self.COLS-1]-(self.prefixSum[i][col2]+self.suffixSum[i][col1])
            i+=1 
        return -res




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)