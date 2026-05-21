# Step1

## アプローチ

* 同時に重複しているのが何個あるかわかればいい
* meetingが開始したら+1, 終了したら-1をするようなdiff配列を用意
    * O(N)
* その和を前から計算して, 最大値分の部屋が必要
* あるいは, intervalのendに合わせてソートをした上で, 直前に終わったミーティング時刻と今から予約しようとするミーティングの開始時刻の関係を見てもいい
    * ただ, 重複の個数を数える必要はある
    * 現在の重複数と, 重複数が増える場合の開始時間の境目がわかるとよさそう
    * O(NlogN)

## Code1-1 (diff)

```python
MAXIMUM_END_TIME = 10**6


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        ongoing_meeting_diff = [0] * (MAXIMUM_END_TIME + 1)
        for interval in intervals:
            ongoing_meeting_diff[interval.start] += 1
            ongoing_meeting_diff[interval.end] -= 1
        
        maximum_ongoing_meeting = 0
        ongoing_meeting_sum = 0
        for diff in ongoing_meeting_diff:
            ongoing_meeting_sum += diff
            maximum_ongoing_meeting = max(maximum_ongoing_meeting, ongoing_meeting_sum)
        
        return maximum_ongoing_meeting
        
```

## Code1-2 (endtime sort) - WA

* `intervals=[(1,5),(5,10),(10,15),(15,20),(1,20),(2,6)]`でWA
* 直前とかぶっているかは判定できても, 何個被るかを正しく判定できていない

```python
class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if not intervals:
            return 0

        endtime_ascending_intervals = sorted(intervals, key=lambda interval : (interval.end, interval.start))

        previous_endtime = -1
        rush_hour_endtime = -1
        used_rooms = 1
        maximum_num_rooms = 1
        for interval in endtime_ascending_intervals:
            # 直前の予約と被らない
            if previous_endtime <= interval.start:
                used_rooms = 1
                previous_endtime = interval.end
                continue

            # 直前の予約とのみ被る
            if rush_hour_endtime <=  interval.start < previous_endtime:
                used_rooms = 2
                maximum_num_rooms = max(maximum_num_rooms, used_rooms)
                rush_hour_endtime = previous_endtime
                previous_endtime = interval.end
                continue
                
            # 部屋を増やさないと対応不可
            used_rooms += 1
            maximum_num_rooms = max(maximum_num_rooms, used_rooms)
            previous_endtime = interval.end

        return maximum_num_rooms

```

# Step2

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/57
    * 主には, 自分のcode1-1(diff)と同様の解法
        * 該当リポジトリのコメントより
            * > 私、この問題を手で解くとして、解法の取りうる範囲の数字を全部挙げはじめたら結構驚くと思うんですよね。浮動小数点だったらこのままでは駄目ですよね。
        * 座標圧縮やタプルへの変変などを取り入れている
* https://github.com/naoto-iwase/leetcode/pull/57
    * heapに使用中の部屋の終了時刻を保存する実装
        * 予約が来た時に
            * 今の使用中の部屋の終了時刻のうち最も早いものが, 予約の開始時刻よりも早い場合
                * 使用中の部屋の終了時刻のうち最も早いものをsいしてt, 代わりに今来た予約を取る
            * それ以外
                * 部屋を追加して新しい予約を取る
    * 開始時刻, 終了時刻それぞれがイベントの発火時刻とする実装
        * 時刻を進めていって起きるイベントごとに現在の使われている部屋の数を更新する
        * 座標圧縮版のcode1-1をより効率的にしたイメージ

## 上記を踏まえていくつか実装

### Code2-1 (diff_with_compression)

* start, endの時刻でそれぞれ+1, -1をした累積和を計算する方法に座標圧縮を加えたもの
* len(intervals)=Nとして計算量を考える
* 座標圧縮では, intervalsの開始時刻, 終了時刻の順序をランクとして表現する
    * 2Nの要素をsortして小さい順にランクを割り振る
        * 時間: O(NlogN)
        * 空間: O(N)
* ランクの最大値分の長さの配列`diff`を用意する
    * 値に被りがない場合, rankの最大値は2N
    * 空間: O(N)
* 圧縮された`interval`ごとに`start`と`end`のランクに対応する位置の`diff`をそれぞれ`+1`, `-1`する
* `diff`の累積和を先頭から確認していった時の最大値が必要な部屋の数の最大数
    * 時間: O(N)
* 総じて,
    * 時間: O(NlogN)
        * 実行時間の見積もり: 500log500 / 10^6 ^= 10^-4 secくらい
    * 空間: O(N)
        * 使用スペースの見積もり: 2 * 28 byte(intあたり) * 500 / 1024 ~= 28KBくらい

```python
import itertools


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        compressed_intervals, num_ranks = self._compress_intervals(intervals)

        ongoing_meetings_diff = [0] * num_ranks
        for compressed_interval in compressed_intervals:
            ongoing_meetings_diff[compressed_interval.start] += 1
            ongoing_meetings_diff[compressed_interval.end] -= 1

        accumulated_sum = list(itertools.accumulate(ongoing_meetings_diff))

        return max(accumulated_sum, default=0)


    def _compress_intervals(self, intervals: list[Interval]) -> tuple[list[Interval], int]:
        times_set = set()
        for interval in intervals:
            times_set.add(interval.start)
            times_set.add(interval.end)
        
        times_list = sorted(times_set)

        time_to_rank = {}
        for i, time in enumerate(times_list):
            time_to_rank[time] = i
        num_ranks = len(times_list)

        compressed_intervals = []
        for interval in intervals:
            compressed_interval = Interval(
                time_to_rank[interval.start],
                time_to_rank[interval.end]
            )
            compressed_intervals.append(compressed_interval)

        return compressed_intervals, num_ranks

```

### Code2-3 (heap)

* 使用中の部屋の終了時刻を追う
* 予約の時刻が来るたびに, 
    * すでに使用中の部屋で予約の時刻より早いものがあれば解放して新しい予約を入れる
    * 解放できる予約がなかったら, 新しい部屋を追加して予約を入れる
* 最初に`intervals`を開始時刻でソートする
    * 時間: O(NlogN)
* そのあと, `intervals`の各要素について,
    * 使用中の部屋の終了時刻を表す`heap`にpushやpopをする
    * `heap`に入っている要素の数は使用する部屋の数分
    * 最悪の計算量となる場合は, log1 + log2 + ... + logNだから, 計算量はO(log(N!))かな
        * スターリングの近似で, O(NlogN)とできる
* 空間計算量は, 
    * heapに最大でN個の要素が入るからO(N)

```python
import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda interval : interval.start)

        release_times = []
        for interval in sorted_intervals:
            if release_times and release_times[0] <= interval.start:
                heapq.heapreplace(release_times, interval.end)
            else:
                heapq.heappush(release_times, interval.end)
        
        return len(release_times)

```

### Code2-4 (two poitner)

* ミーティングの開始時刻と終了時刻それぞれの変化を追う
* 開始時刻だけの配列と終了時刻だけの配列を用意してそれぞれにポインタを用意する方法が参考にしたPRではあった
* よく考えたら, タプルにして(時刻, startかendのどちらかを表すフラグ)とすれば一つの配列でもいける
* そしたら, 結局やっていることは, Code*-1(diff)のコードとほぼ同じだな
* これも, `interval`の長さをNとすると
    * タプルの配列の長さが2Nになるので, それのソートにO(NlogN)の計算
    * その後, タプルの各要素について処理を行うのでO(N)
* 空間計算量は,
    * タプルの配列を用意するのでO(N)

```python
TYPE_START = 1
TYPE_END = 0

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:

        time_and_type = []
        for interval in intervals:
            time_and_type.append((interval.start, TYPE_START))
            time_and_type.append((interval.end, TYPE_END))

        time_and_type = sorted(time_and_type)

        max_used = 0
        ongoing_meetings = 0
        for _, time_type in time_and_type:
            if time_type == TYPE_START:
                ongoing_meetings += 1
            else:
                ongoing_meetings -= 1

            max_used = max(max_used, ongoing_meetings)

        return max_used

```

# Step3

## Code3-3 (heap)

* 実際に予約が全部来る前でもリアルタイム的に処理できそうだと思ったので, heapの解法をstep3で実装する

```python
import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval : interval.start)

        release_times = []
        for interval in sorted_intervals:
            if release_times and release_times[0] <= interval.start:
                heapq.heapreplace(release_times, interval.end)
            else:
                heapq.heappush(release_times, interval.end)
        
        return len(release_times)

```

