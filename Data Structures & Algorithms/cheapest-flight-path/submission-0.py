class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minHeap = [(0, src, k + 1)]
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for u, v, w in flights:
            adj[u].append((v, w))
        
        visited_stops = {} # node -> remaining_stops
        while minHeap:
            cost, n1, stops = heapq.heappop(minHeap)
            if n1 == dst:
                return cost
            if stops > 0:
                if n1 in visited_stops and visited_stops[n1] >= stops:
                    continue
                visited_stops[n1] = stops
                for n2, w2 in adj[n1]:
                    heapq.heappush(minHeap, (cost + w2, n2, stops - 1))
        return -1