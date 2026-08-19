"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        #time:change in rooom number 
        rooms=defaultdict(int)

        for interval in intervals:
            rooms[interval.start]+=1
            rooms[interval.end]-=1 

        res=0
        curr_sum=0
        for k in sorted(rooms):
            curr_sum+=rooms[k]
            res=max(res,curr_sum)
        return res