class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        eventN = 0

        for i in nums:
            count = 0
            while i >0 :
                i //= 10
                count += 1
            if count % 2 == 0 :
                eventN +=1

        return eventN
        