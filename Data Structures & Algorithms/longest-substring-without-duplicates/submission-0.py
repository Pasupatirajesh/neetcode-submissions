class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cmap =set()
        l, r = 0, 0
        ml = 0
        for r in range(len(s)):
            while s[r] in cmap:
                cmap.remove(s[l])
                l+=1
            cmap.add(s[r])
            ml = max(ml, r-l+1)
        return ml 

        