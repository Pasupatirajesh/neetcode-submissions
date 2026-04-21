class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sq = [set() for _ in range(9)]

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):

                num = board[r][c]
                sq_index = (r //3) * 3 + (c // 3)

                if num == '.':
                    continue

                if (num in rows[r] or num in cols[c] or num in sq[sq_index]):
                    return False
                rows[r].add(num)
                cols[c].add(num)
                sq[sq_index].add(num)

        return True 
                
