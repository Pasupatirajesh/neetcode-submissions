class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num, f in count.items():
            if f == 1:
                return num
      
