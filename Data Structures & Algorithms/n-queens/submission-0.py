class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        result = []

        def isSafe(row, col):
            for i in range(col):
                if board[row][i] == "Q":
                    return False
            
            #Check upper left diagonal
            i, j = row, col
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j-=1
            
            #check lower left diagonal
            i, j = row, col
            while i< n and j >=0:
                if board[i][j] == 'Q':
                    return False
                i+=1
                j-=1
            return True

        def backtrack(col):
            if col == n:
                result.append(["".join(r) for r in board])
                return
            for row in range(n):
                if isSafe(row, col):
                    board[row][col] = 'Q'
                    backtrack(col+1)
                    board[row][col] = "."
        
        backtrack(0)
        return result
