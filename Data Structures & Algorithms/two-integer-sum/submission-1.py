class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numdict:
                return [numdict[diff], i]
            numdict[nums[i]] = i
        
        