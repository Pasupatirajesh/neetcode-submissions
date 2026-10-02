class Solution:
    def maxDifference(self, s: str) -> int:
        max_diff = 0
        oddf = 0 
        evenf = len(s)
        count = Counter(s)
        for char,freq in count.items():
            if freq % 2 != 0:
                oddf = max(oddf, freq)
            else:
                evenf = min(evenf, freq)
        max_diff = max(max_diff, (oddf-evenf))
        return oddf-evenf
