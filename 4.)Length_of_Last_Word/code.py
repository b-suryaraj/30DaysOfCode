class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last=s.split()
        m=len(last)
        n=len(last[m-1])
        return n
