class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        count_n = Counter(nums)
        for el, freq in count_n.items():
            if freq > (n / 3):
                res.append(el)
        return res 

