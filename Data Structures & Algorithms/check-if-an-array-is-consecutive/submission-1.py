class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        unique = set(nums)
        return len(unique) == len(nums) and max(nums)- min(nums)+1 == len(nums)

