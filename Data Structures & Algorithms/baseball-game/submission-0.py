class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:  
            if operation == "+":
                if len(stack) >= 2:
                    res = stack[-1] + stack[-2]
                    stack.append(res)
            elif operation == 'C':
                if stack:
                    stack.pop()
            elif operation == 'D':
                if stack:
                    res = stack[-1] * 2
                    stack.append(res)
            else:
                stack.append(int(operation))
        return sum(stack) if stack else 0

