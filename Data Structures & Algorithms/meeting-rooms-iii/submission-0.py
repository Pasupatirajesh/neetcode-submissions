class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda m:m[0]) #sorting is m log m + (m log n)
        available, busy = [i for i in range(n)], []
        count = [0] * n
        for start, end in meetings:
            #finish meetings
            while busy and start >= busy[0][0]:
                _ , roomnumber = heapq.heappop(busy)
                heapq.heappush(available, roomnumber)
            
            if not available:
                endt, roomnum = heapq.heappop(busy)
                end = endt + (end-start)
                heapq.heappush(available, roomnum)
            # room is available
            
            room = heapq.heappop(available)
            heapq.heappush(busy, (end, room))
            count[room]+=1

        return count.index(max(count))