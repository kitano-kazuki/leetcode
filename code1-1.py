class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        end_time_ascending_intervals = sorted(intervals, key=lambda interval: (interval.end, interval.start))
        for i in range(1, len(end_time_ascending_intervals)):
            previous_interval = end_time_ascending_intervals[i - 1]
            interval = end_time_ascending_intervals[i]
            if interval.start < previous_interval.end:
                return False
            
        return True
