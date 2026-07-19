class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        current_max = -1
        for val, freq in count.items():
            if freq == 1:
                current_max = max(current_max, val)
        return current_max if current_max else -1