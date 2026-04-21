class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        board = [['.' for _ in range(n)] for _ in range(n)]

        
        def isSafe(r, c):
            for i in range(c):
                if board[r][i] == 'Q':
                    return False
            
            i, j = r, c
            while i >= 0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j-=1
            
            i,j = r, c
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i+=1
                j-=1
            
            return True


        def backtrack(col):
            if col == n:
                result.append([''.join(r) for r in board])
                return
            for row in range(n):
                if isSafe(row, col):
                    board[row][col] = 'Q'
                    backtrack(col+1)
                    board[row][col] = '.'
        
        backtrack(0)
        return result
            
        