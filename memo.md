# Step1

## アプローチ

* `intervals`が与えられて、そこに`newInterval`を挿入する
* どの位置に挿入するかを開始時刻を見て探す
* 挿入する手前のインターバルと`newInterval`がかぶっていたら`newInterval`の開始時刻は使わない
* 終了時刻が他のどのインターバルまで被るかをしりたい
* newInterval.end <= intervals[i].startとなる最小のiをさがす
* 自然言語で整理し直す
    * まずは, 挿入位置を探す
    * `newInterval.start <= intervals[i].start`となる最小の`i`を探す
    * `i = 0`あるいは`intervals[i - 1].end <= newInterval.start`となっていれば, 自分より前のintervalと被ることはない
        * `intervals[i - 1].end <= newInterval.end <= intervals[i].start`だったら, 新しく挿入するだけ
    * `newInterval.start <= intervals[i - 1].end`だったら, 直前のintervalとかぶっているので, 開始地点に関しては`intervals[i - 1]`に統合される
        * このとき, さらに`newInterval.end <= intervals[i - 1].end`だったら、挿入は完全に無意味
        * `intervals[i - 1].end <= newInterval.end <= intervals[i].start`だったら, 前の区間のendを変えるだけ
        * `intervals[i].start <= newInterval.end`だったら, 絶対に1以上の既存のintervalとかぶっている
        * `newInterval.end <= intervals[j].start`となる最小の`j`を探す
        * `intervals[j - 1].end <= newInterval.end`だったら, 新しい区間は`i~j`の既存のインターバルを潰す
        * `newInterval.end <= intervals[j - 1]`だったら, 新しい区間は`i~j`をつぶした上で, endを`intervals[j-1]`にしたもの
* `start`の調整と`end`の調整で共通する部分が多そう
    * かぶっている場合は`newInterval`の`start`や`end`を置き換えた上で、もともとのかぶっていたものを削除して、新しく挿入と捉え直す

## Code1-1 (Bisect)

* AC: 28:32
* 結構てこずった
* 最後に、無理やり区間をマージしているけどそれ以外の最良の方法あるかな？？
* 時間計算量は, O(N)

```python
import bisect


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]
        
        intervals_after_insertion = []
        interval_for_insertion = [None, None]

        insert_index = bisect.bisect_left(intervals, newInterval[0], key=lambda x: x[0])
        # newIntervalの開始が直前のintervalと被らない
        if insert_index == 0 or intervals[insert_index - 1][1] <= newInterval[0]:
            interval_for_insertion[0] = newInterval[0]
            intervals_after_insertion.extend(intervals[:insert_index])
        else:
            interval_for_insertion[0] = intervals[insert_index - 1][0]
            intervals_after_insertion.extend(intervals[:insert_index - 1])

        behind_index = bisect.bisect_left(intervals, newInterval[1], key=lambda x: x[0])
        # newIntervalの終了が直前のintervalと被らない
        if behind_index == 0 or intervals[behind_index - 1][1] <= newInterval[1]:
            interval_for_insertion[1] = newInterval[1]
        else:
            interval_for_insertion[1] = intervals[behind_index - 1][1]
        intervals_after_insertion.append(interval_for_insertion)
        intervals_after_insertion.extend(intervals[behind_index:])

        result = []
        start = intervals_after_insertion[0][0]
        end = intervals_after_insertion[0][1]
        i = 1
        while i < len(intervals_after_insertion):
            if intervals_after_insertion[i][0] == end:
                end = intervals_after_insertion[i][1]
                i += 1
                continue
            result.append([start, end])
            start = intervals_after_insertion[i][0]
            end = intervals_after_insertion[i][1]
            i += 1
        
        result.append([start, end])

        return result


```

# Step2

## Code2-1 (Bisect)

* overlapがないから, `bisect.bisect_left`を`end`に対しても行えた

```python
import bisect
import operator


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]

        start, end = newInterval
        
        start_index = bisect.bisect_left(intervals, start, key=operator.itemgetter(0))
        if start_index > 0 and intervals[start_index - 1][1] >= start:
            start = intervals[start_index - 1][0]
            start_index -= 1

        end_index = bisect.bisect_left(intervals, end, key=operator.itemgetter(1))
        if end_index < len(intervals) and intervals[end_index][0] <= end:
            end = intervals[end_index][1]
            end_index += 1
        
        return intervals[:start_index] + [[start, end]] + intervals[end_index:]


```

## 他の人のPRを見る

* https://github.com/naoto-iwase/leetcode/pull/72
    * スライス代入を使うことでシンプルに描ける&in-placeにも対応可能
    * O(N)で処理する解法
        * new_start, new_end = newIntervalとする
        * new_startよりも早い時間に終了するintervalはそのまま活用
        * new_endよりも遅い時間に開始するインターバルはそのまま活用
        * new_startよりも遅い時間に終了する, かつ,new_endよりも早い時間に開始するインターバルは適切に処理をするべき
            ```bash
              |------|     <- newInterval
            |--|
                |-|        
                    |----| 
            ```
            * つまり, 区間が被っているということ
            * startをそれらの中での一番早い奴ら
            * endをそれらの中での一番遅い奴らにする

## Code2-2 (Linear)

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        intervals_after = []

        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            intervals_after.append(intervals[i])
            i += 1
        
        # newIntervalとoverlap
        start = newInterval[0]
        end   = newInterval[1]
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            start = min(start, intervals[i][0])
            end   = max(end, intervals[i][1])
            i += 1
        intervals_after.append([start, end])

        while i < len(intervals):
            intervals_after.append(intervals[i])
            i += 1
        
        return intervals_after
        
```

# Step3

## Code3-1 (Bisect)

```python
import bisect
import operator

START = 0
END = 1


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        start = newInterval[START]
        start_index = bisect.bisect_left(intervals, newInterval[START], key=operator.itemgetter(START))
        if start_index > 0 and intervals[start_index - 1][END] >= newInterval[START]:
            start = intervals[start_index - 1][START]
            start_index -= 1

        end = newInterval[END]
        end_index = bisect.bisect_left(intervals, newInterval[END], key=operator.itemgetter(END))
        if end_index < len(intervals) and intervals[end_index][START] <= newInterval[END]:
            end = intervals[end_index][END]
            end_index += 1
        
        return intervals[:start_index] + [[start, end]] + intervals[end_index:]
        
```
