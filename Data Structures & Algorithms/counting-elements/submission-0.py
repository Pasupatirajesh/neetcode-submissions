class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = Counter(arr)
        ans = 0
        for i, num in enumerate(arr):
            if num + 1 in count:
                ans+=1
        return ans
