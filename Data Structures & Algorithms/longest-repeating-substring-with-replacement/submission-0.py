class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxcount = 0
        maxlen = 0 
        cmap ={}

        for r in range(len(s)):
                cmap[s[r]] = 1 + cmap.get(s[r], 0)
                maxcount = max(maxcount, cmap[s[r]])
                while r-l+1 -maxcount > k:
                    cmap[s[l]]-=1
                    l+=1
                maxlen = max(maxlen, r-l+1)
        return maxlen
        

        