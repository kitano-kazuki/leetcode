class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        end_time_ascending_intervals = sorted(intervals, key=lambda interval: (interval.end, interval.start))
        for i in range(1, len(end_time_ascending_intervals)):
            interval_ended_recently = end_time_ascending_intervals[i - 1]
            interval_to_attend = end_time_ascending_intervals[i]
            if interval_to_attend.start < interval_ended_recently.end:
                return False
            
        return True
