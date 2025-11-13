class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_substring = s.split()[-1]
        return len(last_substring)
        