"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startarr = sorted([i.start for i in intervals])
        endarr = sorted([i.end for i in intervals])

        count, res = 0, 0
        s, e = 0, 0
        while s < len(startarr):
            if startarr[s] < endarr[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res = max(res, count)
        return res 