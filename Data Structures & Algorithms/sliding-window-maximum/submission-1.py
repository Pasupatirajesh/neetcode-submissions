class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max_val = 0
        # res = []
        # for i in range(len(nums) -k + 1):
        #     max_val = max(nums[i:i+k])
        #     res.append(max_val)
        # return res 
        res = []
        l, r = 0, 0
        resdeq = collections.deque()
        while r < len(nums):
            while resdeq and nums[resdeq[-1]] < nums[r]:
                resdeq.pop()
            resdeq.append(r)

            if l > resdeq[0]:
                resdeq.popleft()

            if (r+1) >= k:
                res.append(nums[resdeq[0]])
                l+=1
            r+=1
        return res 


