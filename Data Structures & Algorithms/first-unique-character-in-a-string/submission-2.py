class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        n = len(s)
        
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = i
            else:
                count[s[i]] = n
        
        res = n
        for ch in count:
            res =  min(res, count[ch])
        return -1 if res == n else res