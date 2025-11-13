class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_digit = digits[-1] +1
        if last_digit < 10:
            digits[-1] = last_digit
        else:
            digits[-1] = 1
            digits.append(0)

        return digits

        