class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sq = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                num = board[r][c]
                sq_index = (r//3) * 3 + (c//3)
                if num in row[r] or num in col[c] or num in sq[sq_index]:
                    return False
                row[r].add(num)
                col[c].add(num)
                sq[sq_index].add(num)
        return True 