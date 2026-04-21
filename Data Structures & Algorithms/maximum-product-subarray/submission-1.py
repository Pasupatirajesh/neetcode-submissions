from sys import maxsize
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, n):
            num = nums[i]
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)

            max_prod = max(max_prod, cur_max)
        return max_prod
