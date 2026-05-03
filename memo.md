# Step1

* Arai60を結構進めたタイミングで自分の実力がどのくらいついてきたかしりたかったので, Hard問題をやってみる。

## 問題設定の説明

[2402. Meeting Rooms ⅲ](https://leetcode.com/problems/meeting-rooms-iii/description/)

### 日本語で要約

* `0`から`n-1`までのラベルがつけられた会議室がある
* `[start_i, end_i)`としてミーティングを予約したい開始時間と終了時間がいっぱい送られてくる. (送られてくる予約のstart_iは全部違う)
* 以下のルールでミーティングの予約に対して部屋を割り当てる.
    * ミーティングはまだ使われていない部屋の中で一番若い番号の部屋で行う
    * 空いている部屋がなかった場合は, 予約の割り当てを遅延
    * 空いている部屋が生まれた場合は, 遅延されている予約の中から最も元々の開始時刻が早かった予約を割り当てる.
* 一番ミーティングが行われた部屋の番号を知りたい. ただし該当する部屋が複数ある場合はそのうち一番小さいラベル番号のもの.

### 原文

You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

### Constraints

* 1 <= n <= 100
* 1 <= meetings.length <= 105
* meetings[i].length == 2
* 0 <= starti < endi <= 5 * 105
* All the values of start_i are unique.

### Example 1

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 

### Example 2

Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 

## アプローチ

### 時刻を追う方法

* 空いている部屋, 遅延された予約の一覧, 時刻->空く部屋の辞書を用意
* 各時刻ごとに以下の処理を行う
    * その時刻で空く部屋があるかを辞書から探す. 空いている部屋の集合にそれを追加
    * 現在の時刻から始まる予約がある場合は, 遅延された予約一覧の末尾にそれを追加.
    * 空いている部屋が0になるまで、遅延された予約の先頭から部屋を割り当てる
* 実行時間を見積もる
    * 最悪の場合は, 部屋が1個しかないのに, 長い予約が大量にくるとき
        * 5 * 10^5 * 10^5 = 5 * 10^10 stepくらい必要
        * Pythonでは10^4 secほどかかる

### 予約を追う方法

* 上記方法だと無駄が多そう
    * 長い予約があった時に, いちいち時刻を一つ動かして確認する必要はない気がする
* 理想は予約を全部見るだけで済むアプローチ, 10^5 / 10^6 = 0.1 sec程度で実行できる
* 空いている部屋, 遅延された予約の実行にかかる時間リスト, (部屋解放時刻, 部屋番号)のminheapを用意していい感じにできないか.

#### 実験

**入力**
n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]

**手順**

1. 初期値
empty_rooms: 0, 1
postponed: []
release_schedule: []
used: 0->0, 1->0

2. 予約0: `[0, 10)`
empty_rooms: 1
postponed: []
release_schedule: [(10, 0)]
used: 0->1, 1->0

3. 予約1: `[1, 5)`
empty_rooms: 
postponed: []
release_schedule: [(5, 1), (10, 0)]
used: 0->1, 1->1

4. 予約2: `[2, 7)`
* この時は, 時刻2より前に部屋が開放されているかもしれないから確認したい
    * relrease_schedule[0]をみて, 部屋が開放されるのが時刻5(>2)
    * この予約は遅延したい
empty_rooms: 
postponed: [5]
release_schedule: [(5, 1), (10, 0)]
used: 0->1, 1->1

5. 予約3: `[3, 4)`
* relrease_schedule[0]をみて, 部屋が開放されるのが時刻5(>3)
    * この予約は遅延
empty_rooms: 
postponed: [5, 1]
release_schedule: [(5, 1), (10, 0)]
used: 0->1, 1->1

6. 遅延された予約を処理 - 1
* relrease_schedule[0]をみて, 時刻5になったとする
    * 1番の部屋を開放
* potponedをみて 先頭の長さ5の予約を割り当てる
empty_rooms: 
postponed: [1]
release_schedule: [(10, 0), (10, 1)]
used: 0->1, 1->2

6. 遅延された予約を処理 - 2
* relrease_schedule[0]をみて, 時刻10になったとする
    * 0番の部屋を開放
* 残ったrelrease_scheduleも時刻10で開放される
    * 1番の部屋を開放
* potponedをみて 先頭の長さ1の予約を割り当てる

empty_rooms: 1
postponed: []
release_schedule: [(11, 0)]
used: 0->2, 1->2

#### 思ったこと

* 遅延予約の対応
    * 遅延された予約がある場合の処理が複雑になりそうだから整理したい
    * 新しい予約を処理しているが, 遅延された予約が存在するとき
        * 新しい予約を遅延された予約の末尾に加えて, 遅延された予約のみの時の処理をすればいい
    * 新しい予約の開始時刻が, 直近の部屋開放時刻よりも遅かった時
        * 新しい予約の開始時刻よりも前に遅延された予約が処理されているはず
        * 直近の部屋開放時刻が新しい予約の開始時刻よりも遅い時間になるまで, 遅延予約の処理をしたい
        * 最後に処理した遅延予約の処理と同様のことができそう
* SegmentTreeのlazyな更新に少し近い気もした


## Code1-1

```python
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

```

# Step2

## Code2-2

* 関数名`resolve`->`release_and_reserve_until_end_time`
    * 引き数に`end_time`があるなら`release_and_reserve`だけでもいいのかな？？
* 部屋を予約する処理は二箇所で登場しているけど、関数に切り出すほどかは迷った
    * 関数に切り出すとその定義部分まで見に行かないといけない
    * 関数に切り出すとしたら３行だけ
    * 以上の理由から今回は切り出さずにコメントで対応
* 結局heapとかを使ったので計算量がどうなるかを考える
* 各部屋について予約を行う
* 予約が遅延された場合でもそうでない場合でも、予約を確定するタイミングでrelease_timeのheapに挿入
* 次の予約を取る前に、部屋の解放が行われている. 部屋の解放でもempty_roomsのheapに挿入
* O(MlogN)かな？？release_timeもempty_roomsも要素数は最大でN
* あとはソートでO(MlogM)かかる
* 支配的なのはO(MlogM)か.

```python
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

```

# Step3



