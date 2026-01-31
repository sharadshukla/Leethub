class MinStack:

    def __init__(self):
        self.items = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1])) 

    def pop(self) -> None:
        if len(self.items) != 0:
            self.items.pop()
        if len(self.min_stack) != 0:
            self.min_stack.pop()

    def top(self) -> int:
        if len(self.items) != 0:
            return self.items[-1]
        else:
            return 0
        

    def getMin(self) -> int:
        return self.min_stack[-1]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()