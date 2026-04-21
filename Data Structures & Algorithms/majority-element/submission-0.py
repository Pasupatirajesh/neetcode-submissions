class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = Counter(nums)
        n = len(nums)
        for el, count in hash_map.items():
            if count > n /2 :
                return el
