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

        def resolve(time: int) -> None:
            while release_time_and_room and release_time_and_room[0][0] <= time:
                previous_released_time, previous_released_room = heapq.heappop(release_time_and_room)
                heapq.heappush(empty_rooms, previous_released_room)
                while empty_rooms and postponed_durations:
                    duration = postponed_durations.popleft()
                    room = heapq.heappop(empty_rooms)
                    heapq.heappush(release_time_and_room, (previous_released_time + duration, room))
                    room_to_count[room] += 1
            return

        for start, end in meetings:

            resolve(start)

            if empty_rooms:
                room = heapq.heappop(empty_rooms)
                heapq.heappush(release_time_and_room, (end, room))
                room_to_count[room] += 1
                continue

            postponed_durations.append(end - start)

        while release_time_and_room:
            if not postponed_durations:
                break
            previous_released_time, previous_released_room = heapq.heappop(release_time_and_room)
            heapq.heappush(empty_rooms, previous_released_room)
            duration = postponed_durations.popleft()
            room = heapq.heappop(empty_rooms)
            heapq.heappush(release_time_and_room, (previous_released_time + duration, room))
            room_to_count[room] += 1

        most_used_room = None
        most_used_frequency = 0
        for room, frequency in room_to_count.items():
            if frequency > most_used_frequency:
                most_used_frequency = frequency
                most_used_room = room
        
        return most_used_room
