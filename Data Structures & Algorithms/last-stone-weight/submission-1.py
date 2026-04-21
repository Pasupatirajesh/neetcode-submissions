class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = [-stone for stone in stones]

        heapq.heapify(stone_heap)

        while len(stone_heap) > 1:
            x, y = -heapq.heappop(stone_heap), -heapq.heappop(stone_heap)
            if x == y:
                continue
            elif x != y:
                y = -(x-y)
                heapq.heappush(stone_heap, y)
        return -stone_heap[0] if len(stone_heap) == 1 else 0





        