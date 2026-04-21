class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l , r = 0, 0
        while r < len(t) and l < len(s):
            if t[r] == s[l]:
                l+=1     
            r+=1
        return l == len(s)