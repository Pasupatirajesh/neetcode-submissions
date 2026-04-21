class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        S = sum(nums)
        target = S// 2
        if S % 2 != 0:
            return False
        curSum = 0
        
        dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]

        def memo(i, curSum):      
            if curSum == target:
                return True
            if curSum > target or i == n:
                return False
            
            if dp[i][curSum] != -1:
                return dp[i][curSum]
                        
            include = memo(i+1, curSum + nums[i])
            exclude = memo(i+1, curSum)
            dp[i][curSum] = include or exclude
            return dp[i][curSum]
        return memo(0, 0)

            
