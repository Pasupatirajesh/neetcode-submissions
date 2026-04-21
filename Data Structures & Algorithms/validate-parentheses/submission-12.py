class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in '{[(':
                stack.append(s[i])
            if s[i] == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            if s[i] == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            if s[i] == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        return not stack
            
