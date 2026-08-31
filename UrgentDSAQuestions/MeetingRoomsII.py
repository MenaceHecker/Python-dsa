## Given an array of meeting time interval objects consisting of start 
# and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
# find the minimum number of rooms required to schedule all meetings without any conflicts.

import heapq

from aiohttp_retry import List
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x : x.start)
        heap = []
        for interval in intervals:
            start = interval.start 
            end = interval.end
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap,end)
        return len(heap)

        