class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * n

        available = [i for i in range(n)]
        busy = [] #(end, roomnum)

        for start, end in meetings:
            while busy and start >= busy[0][0]:
                _, roomnumber = heapq.heappop(busy)
                heapq.heappush(available, roomnumber)

            if not available:
                endt, room_num = heapq.heappop(busy)
                end = endt + (end-start)
                heapq.heappush(available, room_num)

            room = heapq.heappop(available)     
            heapq.heappush(busy, (end,room))
            count[room]+=1
        return count.index(max(count))
           