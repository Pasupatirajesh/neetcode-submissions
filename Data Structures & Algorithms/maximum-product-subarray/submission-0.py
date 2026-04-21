from sys import maxsize
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSum = -maxsize -1
        for i in range(0, len(nums)):
            curSum = 1
            for j in range(i, len(nums)):
                curSum*=nums[j]
                if curSum > maxSum:
                    maxSum = curSum
        return maxSum
