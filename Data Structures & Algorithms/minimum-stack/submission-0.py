class MinStack:

    def __init__(self):
        # self.capacity = 2
        self.stack = []  
        # self.length = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
