class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = -1
        for i in nums:
            if i != num:
                count = nums.count(i)
                if count > len(nums)//2:
                    return i
                else:
                    num = i


        