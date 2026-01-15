class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        opList = []
        digitD = {}

        for i in digits:
            if i in digitD:
                digitD[i] += 1
            else:
                digitD[i] = 1

        for i in range(100, 1000):
            valid = True
            numD = {}

            for j in str(i):
                j = int(j)
                if j in numD:
                    numD[j] += 1
                else:
                    numD[j] = 1

            for k,v in numD.items():
                if k not in digitD or v > digitD[k]:
                    valid = False
                    break
            if valid and i % 2 == 0:
                opList.append(i)

        return opList