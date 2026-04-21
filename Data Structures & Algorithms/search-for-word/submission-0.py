class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        if len(word) > ROWS* COLS:
            return False
        
        count = Counter(sum(board, []))

        for c, countword in Counter(word).items():
            if count[c] < countword:
                return False
            
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        def dfs(r, c, index):
            if index == len(word): 
                return True
            
            if not( 0<= r< ROWS and 0 <= c < COLS) or board[r][c] != word[index]:
                return False
            
            letter = board[r][c]
            board[r][c] = '#'
            found = (dfs(r-1, c, index+1) or
                    dfs(r+1, c, index+1) or
                    dfs(r, c+1, index+1) or
                    dfs(r, c-1, index+1))
            board[r][c] = letter
            return found
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False