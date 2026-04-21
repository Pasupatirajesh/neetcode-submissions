class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_val = 0
        res = []
        for i in range(len(nums) -k + 1):
            max_val = max(nums[i:i+k])
            res.append(max_val)
        return res 
        