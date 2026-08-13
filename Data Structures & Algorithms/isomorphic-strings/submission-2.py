class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        schar_map, tchar_map = {}, {}
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if c1 in schar_map and schar_map[c1] != c2:
                return False
            if c2 in tchar_map and tchar_map[c2] != c1:
                return False 
            schar_map[c1] = c2
            tchar_map[c2] = c1
        return True 