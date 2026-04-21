class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = [] * len(points)
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(self.heap, [dist, x, y])
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        
        res = []
        while self.heap:
            dist, x, y = heapq.heappop(self.heap)
            res.append([x, y])
        return res 
                

