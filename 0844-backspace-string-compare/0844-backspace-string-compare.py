class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # if s[0] == '#' and len(s) == 1:
        #     return 
        stackS = []
        stackT = []
        for i in s:
            if stackS and i == '#':
                stackS.pop()
            elif i != '#':
                stackS.append(i)

        for i in t:
            if stackT and i == '#':
                stackT.pop()
            elif i != '#':
                stackT.append(i)

        return stackS == stackT
        