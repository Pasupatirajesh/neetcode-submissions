class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in nums_dict:
                nums_dict[nums[i]] = i
            else:
                return [nums_dict[diff], i]