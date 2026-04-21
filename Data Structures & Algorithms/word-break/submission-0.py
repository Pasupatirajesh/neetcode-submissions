class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = {}
        def memo(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordSet and memo(j
                ):
                    dp[i] = True
                    return True
           
            
            dp[i] = False
            return False
        return memo(0)
      
            
    
    