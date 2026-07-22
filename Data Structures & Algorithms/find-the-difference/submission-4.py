class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        for val, freq in t_count.items():
            if t_count[val] > s_count[val]:
                return val