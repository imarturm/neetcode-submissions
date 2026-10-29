"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sort = sorted(intervals, key=lambda interval: interval.start)
        for meeting1, meeting2 in zip(sort, sort[1:]):
            if meeting1.end > meeting2.start:
                return False
        return True