class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token in ["+", "*", "-", "/"]:
                n1 = stack.pop()
                n2 = stack.pop()

                if token == '+':
                    res = n1+ n2
                elif token == '*':
                    res = n1 * n2
                elif token == '-':
                    res = n2 - n1
                elif token == '/':
                    res = int(n2/n1)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1] if stack else 0
