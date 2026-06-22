class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_ct = Counter(nums)
        for num in nums:
            if nums_ct[num] > 1:
                return True
        return False 