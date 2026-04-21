class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = [(0, k)] #stores weight and destination
        visited = set()
     
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        
        for u, v, t in times:
            adj[u].append((v, t))
        
        t = 0
        while minHeap:

            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = t1

            for n2, t2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (t1+t2, n2))
        return t if len(visited) == n else -1 

        
