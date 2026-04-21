class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_heap = []
        heapq.heapify(nums_heap)

        for num in nums:
            heapq.heappush(nums_heap, num)
            while len(nums_heap) > k:
                heapq.heappop(nums_heap)
        return nums_heap[0]

