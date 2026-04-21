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
        deq = collections.deque()
        while r < len(nums):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)

            if l > deq[0]:
                deq.popleft()
            
            if r+1 >= k:
                res.append(nums[deq[0]])
                l+=1
            r+=1
        return res


