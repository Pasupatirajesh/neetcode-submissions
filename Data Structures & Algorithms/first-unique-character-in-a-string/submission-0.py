class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
     
        return next((i for i, ch in enumerate(s) if count[ch]== 1), -1)

