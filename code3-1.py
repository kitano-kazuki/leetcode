import collections
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:

        empty_rooms = list(range(n))
        heapq.heapify(empty_rooms)
        release_time_and_room = []
        postponed_meeting_durations = collections.deque([])
        room_usage_count = [0] * n

        def release_and_reserve_by_endtime(endtime) -> None:
            while release_time_and_room and release_time_and_room[0][0] <= endtime:
                # 部屋を解放
                released_time, released_room = heapq.heappop(release_time_and_room)
                heapq.heappush(empty_rooms, released_room)

                # 部屋を確保
                if postponed_meeting_durations:
                    room = heapq.heappop(empty_rooms)
                    postponed_meeting_duration = postponed_meeting_durations.popleft()
                    heapq.heappush(release_time_and_room, 
                                  (released_time + postponed_meeting_duration, room))
                    room_usage_count[room] += 1
            return

        for start, end in sorted(meetings, key=lambda x: x[0]):
            release_and_reserve_by_endtime(start)

            if not empty_rooms:
                postponed_meeting_durations.append(end - start)
            else:
                room = heapq.heappop(empty_rooms)
                heapq.heappush(release_time_and_room, (end, room))
                room_usage_count[room] += 1

        release_and_reserve_by_endtime(float("inf"))

        max_usage = max(room_usage_count)
        return room_usage_count.index(max_usage)
        
        