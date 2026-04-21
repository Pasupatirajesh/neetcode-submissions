class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(_open, _close):
            if _open == _close == n:
                return res.append(''.join(stack))     
            if _open < n:
                stack.append("(")
                backtrack(_open+1, _close)
                stack.pop()
            if _close <_open:
                stack.append(')')
                backtrack(_open, _close +1)
                stack.pop()
        backtrack(0, 0)
        return res

        