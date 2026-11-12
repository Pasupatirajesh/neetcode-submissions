class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_map, s_map = {}, {}
        if len(s) != len(t):
            return False
        if len(s) == len(t):
            for i in range(len(s)):
                t_map[t[i]] = 1 + t_map.get(t[i], 0)
                s_map[s[i]] = 1 + s_map.get(s[i], 0)
            return t_map == s_map

