class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hash_map = Counter(nums)
        for num, count in hash_map.items():
            if count > (n/2):
                return num
        