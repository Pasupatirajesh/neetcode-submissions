class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(n+1):
            adj[i] = []
        
        for u,v, w in times:
            adj[u].append((v,w))
        
        minHeap =[(0, k)]
        visit = set()
        t = 0
        while minHeap:
            cost, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            t = cost
            visit.add(n1)
            for n2, new_cost in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (t + new_cost, n2))
        return t if len(visit) == n else -1

