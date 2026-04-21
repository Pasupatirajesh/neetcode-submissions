class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
       
        for num in nums:
            if num-1 not in nums_set:
                l = 0
                while num+l in nums_set:
                    l+=1
                longest = max(l, longest)
        return longest 
