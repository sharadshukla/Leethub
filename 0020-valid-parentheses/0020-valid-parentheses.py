class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
                continue
            if not stack:
                return False
            
            if i == ')' and stack[-1] == '(':
                stack.pop()
                continue
            elif i == ']' and stack[-1] == '[':
                stack.pop()
                continue
            elif i == '}' and stack[-1] == '{':
                stack.pop()
                continue
            else:
                return False
        
        return not stack
            
            

        