class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def memo(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if j == len(p):
                dp[(i, j)] = i == len(s)
                return dp[(i, j)]

            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if (j + 1) < len(p) and p[j + 1] == '*':
                # 1. Skip '*' and its preceding char → zero occurrences
                # 2. If first matches, consume a char from s → keep pattern
                dp[(i, j)] = memo(i, j + 2) or (first_match and memo(i + 1, j))
            else:
                dp[(i, j)] = first_match and memo(i + 1, j + 1)

            return dp[(i, j)]

        return memo(0, 0)