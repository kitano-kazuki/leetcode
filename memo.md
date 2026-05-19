# Step1

## アプローチ

* すべてのパターンで被っていないかを見ればいい
    * 時間計算量O(N^2), 実行時間目安 (5 * 10^2)^2 / 10^6 ~= 0.25 sec
* ただ, 無駄が多そう
    * 明らかに開始時刻が離れているペアは見なくていい
* 終わる時間で並び替えをする
    * 一つ一つのミーティングについて, 直前に終わっているはずのミーティングより今の開始時刻が遅いかをみればいい？？
    * O(NlogN)

## Code1-1

```python
class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        end_time_ascending_intervals = sorted(intervals, key=lambda interval: (interval.end, interval.start))
        for i in range(1, len(end_time_ascending_intervals)):
            previous_interval = end_time_ascending_intervals[i - 1]
            interval = end_time_ascending_intervals[i]
            if interval.start < previous_interval.end:
                return False
            
        return True

```

# Step2

## Code2-1

* 変数名の調整

```python
class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        end_time_ascending_intervals = sorted(intervals, key=lambda interval: (interval.end, interval.start))
        for i in range(1, len(end_time_ascending_intervals)):
            interval_ended_recently = end_time_ascending_intervals[i - 1]
            interval_to_attend = end_time_ascending_intervals[i]
            if interval_to_attend.start < interval_ended_recently.end:
                return False
            
        return True

```

# Step3

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/56
    * startに遭遇したら+1, endに遭遇したら-1
    * 全体の和が2にならないようにする
* https://github.com/mamo3gr/arai60/pull/59
    * step1は自分の解法とほぼ同じだが, interval.startをキーにソートしている

## Code3-2 (Accumuration Sum)

```python
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

```

# Step4

```python
class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        endtime_ascending_intervals = sorted(intervals, key=lambda interval : interval.end)

        previous_end_time = -1
        for interval in endtime_ascending_intervals:
            if interval.start < previous_end_time:
                return False
            previous_end_time = interval.end
        
        return True

```