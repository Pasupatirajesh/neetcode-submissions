class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count = len(t)
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                i+=1
            count = len(t) - j
        return count 