class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = set()

        for i in range(9):
            for j in range(9):
                val=board[i][j]

                if val==".":
                    continue

                box=(i//3,j//3)

                if (val,i) in rows or (val,j) in cols or (val,box) in boxes:
                    return False

                rows.add((val,i))
                cols.add((val,j))
                boxes.add((val,box))

        return True