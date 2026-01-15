class Solution:
    def convertToBase7(self, num: int) -> str:
        s =""
        if num < 0:
            absNum = abs(num)
        elif num == 0:
            return "0"
        else:
            absNum = num
        while absNum > 0 :
            s += str(absNum%7)
            absNum //= 7

        if num < 0:
            return "-" + s[::-1]
        else:
            return s[::-1]

        