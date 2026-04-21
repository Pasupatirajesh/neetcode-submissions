class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            if c == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            if c == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            if c == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
        return not stack
                    