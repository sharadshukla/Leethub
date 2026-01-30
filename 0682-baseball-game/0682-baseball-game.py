class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for i in operations:
            if i == '+':
                stack.append(stack[-2] + stack[-1])
            elif i == 'D':
                stack.append (2*stack[-1])
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        
        for i in stack:
            sum += i
        
        return sum



        