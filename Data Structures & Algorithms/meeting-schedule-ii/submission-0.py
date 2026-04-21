class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startarr = sorted([i.start for i in intervals])
        endarr = sorted([i.end for i in intervals])
        res = 0
        count = 0
        s = 0
        e = 0
        while s < len(intervals):
            if startarr[s] < endarr[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res = max(res, count)
        return res