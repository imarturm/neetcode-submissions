"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from bisect import insort, bisect_right

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for a, b in zip(intervals, intervals[1:]):
            if a.end > b.start:
                return False
        return True