class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        end_time_ascending_intervals = sorted(intervals, key=lambda interval : interval.end)

        previous_end_time = -1
        for interval in end_time_ascending_intervals:
            if interval.start < previous_end_time:
                return False
            previous_end_time = interval.end
        
        return True
