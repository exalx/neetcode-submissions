class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            if not self.checkList(row):
                return False
            column = []
            for r in range(9):
                column.append(board[r][i])
            if not self.checkList(column):
                return False
            I, J = i // 3, i % 3
            square = []
            for r in range(3):
                for c in range(3):
                    square.append(board[3*I+r][3*J+c])
            if not self.checkList(square):
                return False
        return True
        
    def checkList(self, l: List[str]) -> bool:
        seen = set()
        for s in l:
            if s != ".":
                n = int(s)
                if n in seen:
                    return False
                seen.add(int(n))
        return True
            
