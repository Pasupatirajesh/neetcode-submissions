class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_queries = sorted((q,i) for i,q in enumerate(queries))
        res = [-1] * len(queries)
        intervals.sort(key=lambda it:it[0])
        min_heap = []
        i =0
        
        for q, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r-l+1,r))
                i+=1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            if min_heap:
                res[idx] = min_heap[0][0]
            else:
                res[idx] = -1
        return res