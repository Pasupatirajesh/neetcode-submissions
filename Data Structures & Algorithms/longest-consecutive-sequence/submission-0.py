class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        seq_len = 0
        for i in range(len(nums)):
            if nums[i]-1 not in num_set:
                l = 0
                while (nums[i]+l) in num_set:
                    l+=1
                seq_len = max(l, seq_len)
        return seq_len



        