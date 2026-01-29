class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
                continue
            if s[0] in ")]}":
                return False
            if stack:
                if i is ')' and stack[-1] is '(':
                    stack.pop()
                    continue
                elif i is ']' and stack[-1] is '[':
                    stack.pop()
                    continue
                elif i is '}' and stack[-1] is '{':
                    stack.pop()
                    continue
        
        if not stack:
            return True
        else:
            return False
            
            

        