class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones = 0
        localones = 0
        for num in nums:
            localones= localones+1 if num else 0
            maxones = max(maxones, localones)
        return maxones
        