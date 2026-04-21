class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        dp = [[-1 for _ in range(2 * total + 1)] for _ in range((len(nums)+1))]
        curr_sum = 0
        def memo(i, curr_sum):
            if i == len(nums):
                return 1 if curr_sum == target else 0 
            
            if dp[i][curr_sum + total] != -1:
                return dp[i][curr_sum + total]
            
            op1 = memo(i+1, curr_sum+nums[i])
            op2 = memo(i+1, curr_sum-nums[i])

            dp[i][curr_sum + total] = (op1 + op2)

            return dp[i][curr_sum+ total]
        
        return memo(0, 0)
            



        