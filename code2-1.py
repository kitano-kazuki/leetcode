import heapq
import collections

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        if n <= 0:
            raise ValueError("n must be positive integer.")
        if not meetings:
            return 0

        meetings = sorted(meetings, key=lambda x: x[0])
        empty_rooms = list(range(n))
        postponed_durations = collections.deque([])
        release_time_and_room = []
        room_to_count = {room: 0 for room in range(n)}

        def release_and_reserve_until_endtime(endtime: int | float) -> None:
            while release_time_and_room and release_time_and_room[0][0] <= endtime:
                # 部屋を開放
                released_time, released_room = heapq.heappop(release_time_and_room)
                heapq.heappush(empty_rooms, released_room)

                # 部屋を予約
                if postponed_durations:
                    duration = postponed_durations.popleft()
                    room = heapq.heappop(empty_rooms)
                    heapq.heappush(release_time_and_room, (released_time + duration, room))
                    room_to_count[room] += 1
            return

        for start, end in meetings:
            release_and_reserve_until_endtime(start)

            if not empty_rooms:
                postponed_durations.append(end - start)
            else:
                # 部屋を予約
                room = heapq.heappop(empty_rooms)
                heapq.heappush(release_time_and_room, (end, room))
                room_to_count[room] += 1

        release_and_reserve_until_endtime(float("inf"))

        # 最も使用された一番若い部屋を取得
        most_used_room = None
        most_used_frequency = 0
        for room, frequency in room_to_count.items():
            if frequency > most_used_frequency:
                most_used_frequency = frequency
                most_used_room = room
        
        return most_used_room
