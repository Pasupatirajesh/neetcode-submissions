class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = Counter(arr)
        ans = 0
        for num in arr:
            if num + 1 in count:
                ans+=1
        return ans
