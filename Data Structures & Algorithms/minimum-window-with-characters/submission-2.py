class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        tMap = {}
        windowMap = {}

        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        
        have = 0
        need = len(tMap)

        res, resLen = [-1,-1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            windowMap[c] = 1 + windowMap.get(c, 0)

            if c in tMap and windowMap[c] == tMap[c]:
                have+=1
            
            while have == need:
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = (r-l+1)
                
                windowMap[s[l]]-=1
                if s[l] in tMap and windowMap[s[l]] < tMap[s[l]]:
                    have-=1
                l+=1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""