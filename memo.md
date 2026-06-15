# Step1

## アプローチ

* 重なっているintervalをマージする
* 開始時刻が早いintervalから見ていく
    * intervals[i]を見ているとする
    * intervals[i + 1]の開始時間より, intervals[i]の終了時間が早い
        * intervals[i]は他と被らない
    * intervals[i + 1]の開始時間より, intervals[i]の終了時間が遅い
        * intervals[i + 1]の終了時間よりも, intervals[i]の終了時間が早い
            * intervals[i + 1]を消して, intervals[i]の終了時間をintervals[i + 1]の終了時間にする
        * intervals[i + 1]の終了時間よりも, intervals[i]の終了時間が遅い
            * intervals[i + 1]を消す
* 計算量: O(N) (ソート済みではないならO(NlogN)でソート)
* ここまで5:50

## Code1-1

* AC: 6:19

```python
import operator


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        intervals = sorted(intervals, key=operator.itemgetter(0))

        merged_intervals = [intervals[0]]
        i = 1
        while i < len(intervals):
            _, previous_end = merged_intervals[-1]
            start, end = intervals[i]
            if previous_end < start:
                merged_intervals.append(intervals[i])
                i += 1
                continue
            if previous_end < end:
                merged_intervals[-1][1] = end
                i += 1
                continue
            i += 1
            continue
    
        return merged_intervals
            
```

# Step2

## Code2-1

* 変更なし

```python
import operator


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        intervals = sorted(intervals, key=operator.itemgetter(0))

        merged_intervals = [intervals[0]]
        i = 1
        while i < len(intervals):
            _, previous_end = merged_intervals[-1]
            start, end = intervals[i]
            if previous_end < start:
                merged_intervals.append(intervals[i])
                i += 1
                continue
            if previous_end < end:
                merged_intervals[-1][1] = end
                i += 1
                continue
            i += 1
            continue
    
        return merged_intervals
            
```

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/45
    * マージしたインターバルが確定したタイミングで結果に格納している
    * 自分のコードも`for`ループで回すように改変はできそう
    * odaさんのコメント
        * > これを不要とするために last_interval の代わりに、merged_intervals.last() で代用する手はあるんですが、こっちのほうがいいかもしれませんね。
        * 自分の方法は, `merged_intervals.last()`で代用する方法にあたる
    *  後ろに新しいintervalを加えられるかどうかを毎回毎回判定していると考えた方がわかりやすかったため

# Step3

## Code3-1

```python
import operator


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        intervals = sorted(intervals, key=operator.itemgetter(0))

        merged_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            last_end = merged_intervals[-1][1]
            start, end = intervals[i]
            if last_end < start:
                merged_intervals.append(intervals[i])
            else:
                merged_intervals[-1][1] = max(last_end, end)
        
        return merged_intervals

```