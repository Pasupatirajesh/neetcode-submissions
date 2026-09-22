class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones = 0
        localones = 0
        for num in nums:
            if num == 1:
                localones+=1
            else:
                localones = 0
            maxones = max(maxones, localones)
        return maxones
        