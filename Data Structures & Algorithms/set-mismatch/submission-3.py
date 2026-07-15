class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        ans = [0] * 2

        for i in range(1, n+1):
            if count[i] == 2:
                ans[0] = i
            elif count[i] == 0:
                ans[1] = i
        return ans 