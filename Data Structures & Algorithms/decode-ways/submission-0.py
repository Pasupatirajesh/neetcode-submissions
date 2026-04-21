class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [-1] * (len(s)+1)
        def memo(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]
            res = memo(i+1)
            if i +1 < len(s) and 10 <= int(s[i:i+2]) <=26:
                res += memo(i+2)
            
            dp[i] = res

            return res
        return memo(0)

