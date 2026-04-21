
class Solution:
        
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_heap=[]
        intervals.sort(key=lambda it:it.start)

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
        return len(min_heap)