MAXIMUM_MEETING_ENDTIME = 10**6


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        ongoing_meeting_diff = [0] * (MAXIMUM_MEETING_ENDTIME + 1)

        for interval in intervals:
            ongoing_meeting_diff[interval.start] += 1
            ongoing_meeting_diff[interval.end] -= 1
        
        num_on_going_meetings = 0
        for diff in ongoing_meeting_diff:
            num_on_going_meetings += diff
            if num_on_going_meetings >= 2:
                return False
            
        return True
