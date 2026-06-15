# Step1

## アプローチ

* 普通の辞書にtimestamp機能を加えたものを作りたい
* `set`と`get`の呼ばれる回数の合計は`2 * 10^5`回
* キーごとに, timestampとvalueが存在している
* キーごとにtimestamp順に並べたvalueを配列として持っておく
* getのときのtimestampでその配列から欲しいものを二分探索で探す
* 仮にkeyに対してtimestampN個分の要素があったとすると, その探索にはO(logN)
* すべての`set`呼び出しに対して, 上記の探索が行われるとして
* O(NlogN)
* 実行時間は, 10^5 * log10^5 / 10^6 ~= 1secくらい

## Code1-1

* AC: 13:25

```python
import collections
import dataclasses
import bisect


@dataclasses.dataclass
class TimeData:
    timestamp: int
    value: str


class TimeMap:

    def __init__(self):
        self.key_to_timedatum = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_timedatum[key].append(TimeData(timestamp, value))
        return

    def get(self, key: str, timestamp: int) -> str:
        if not self.key_to_timedatum[key]:
            return ""
        index = bisect.bisect_right(self.key_to_timedatum[key], timestamp, key=lambda timedata: timedata.timestamp)
        if index == 0 :
            return ""
        return self.key_to_timedatum[key][index - 1].value

```

# Step2

## Code2-1

* 変更なし

```python
import collections
import dataclasses
import bisect


@dataclasses.dataclass
class TimeData:
    timestamp: int
    value: str


class TimeMap:

    def __init__(self):
        self.key_to_timedatum = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_timedatum[key].append(TimeData(timestamp, value))
        return

    def get(self, key: str, timestamp: int) -> str:
        if not self.key_to_timedatum[key]:
            return ""
        index = bisect.bisect_right(self.key_to_timedatum[key], timestamp, key=lambda timedata: timedata.timestamp)
        if index == 0 :
            return ""
        return self.key_to_timedatum[key][index - 1].value

```

## 他の人のPRを見る

* https://github.com/TaisukeFujise/leetcode_tafujise/pull/19
    * 解き方は同じ
    * 最初に線形探索の場合の実行時間の見積もりをしているの良い
* https://github.com/huyfififi/coding-challenges/pull/47

# Step3

## Code3-1

* 3:17
* 1:28
* 1:47

```python
import collections
import bisect
import dataclasses


@dataclasses.dataclass
class TimeData:
    timestamp: int
    value: str


class TimeMap:

    def __init__(self):
        self.key_to_timedatum = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_timedatum[key].append(TimeData(timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.key_to_timedatum[key]:
            return ""
        index = bisect.bisect_right(self.key_to_timedatum[key], timestamp, key=lambda x: x.timestamp)
        if index == 0:
            return ""
        return self.key_to_timedatum[key][index - 1].value

```