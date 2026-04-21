class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone_1 = -heapq.heappop(heap)
            stone_2 = -heapq.heappop(heap)
            if stone_1 == stone_2:
                continue
            elif stone_1 != stone_2:
                y = -(stone_2 -stone_1)
                heapq.heappush(heap, -y)
        return -heap[0] if len(heap) == 1 else 0
