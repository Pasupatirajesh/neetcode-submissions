class Solution:
    def romanToInt(self, s: str) -> int:
        romanhash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)):
            if i+1 < len(s) and romanhash[s[i]] < romanhash[s[i+1]]:
                total -= romanhash[s[i]]
            else:
                total+=romanhash[s[i]]
        return total

