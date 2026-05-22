# Step1

## 条件の確認

* 与えられる文字数と行数はそれぞれどのくらいか
    * 文字数: 1 <= s.length <= 1000
    * 行数: 1 <= numRows <= 1000
* 与えられる文字は何が来ても大丈夫そう. スペースが来るかどうかはアプローチによってはバグになり得る？？
* 空文字もあり得るか?
    * 文字数の長さが1以上だからない

## アプローチ

* 自分でグリッドを用意しておいて, 実際に文字を配置していく
    * リストをnumRows用意
    * 方向を管理
    * 今の自分の方向と入れるべきリスト, 見ている文字を教えてもらう
        * それをリストに追加
        * 次の引き継ぎ
* 計算量
    * `s.length`分文字列を見る: O(N)
    * リストに追加する: O(1)
    * リストの中身を全部繋げて出力: O(N)
    * O(N)
* 実行時間: 1000 / 10^6 ~= 10^-3 sec
* 空間計算量:
    * N個の文字が入るリストが別で存在する
    * O(N)
* 使用する容量: 1byte * 1000 ~= 1000 byte ~= 1KB
    * TODO: Pythonにおけるstringの文字が占めるbyteを調べる
* 頑張れば空間計算量をO(1)にすることもできそう・・・？
* 文字列の長さと同じ分だけ配列を確保（答えに使用する配列）
* 各行に入っている文字の個数がわかっていれば、対応する配列のインデックスが導けそう
* ここまで7:37

## Code1-1

* 5:38

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        row_chars = [[] for _ in range(numRows)]
        row = 0
        direction = 1
        for ch in s:
            row_chars[row].append(ch)

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row += direction

        zigzag_chars = []
        for ch_list in row_chars:
            zigzag_chars.extend(ch_list)
        
        return "".join(zigzag_chars)
        
```

# Step2

## Code2-1

* 空間計算量をO(1)にしてみる
* 31:50かかった
* 各行ごとに見るべき文字列を探す
    * 見るべき文字列は, `2 * numRows - 2`文字ごとのサイクルで現れる
    * それとは別に, 最初の行と最後の行以外はななめに上がっていく部分の文字列も見たい
    * それは, 下に`numRows - 今いるrow`分下がって, 再び上に`numRows - 今いるrow`分進んだ場所

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)

        if numRows == 1 or numRows >= n:
            return s
        
        cycle = 2 * numRows - 2

        zigzag_chars = []
        for row in range(numRows):
            for i in range(row, n, cycle):
                zigzag_chars.append(s[i])

                if 1 <= row <= numRows - 2:
                    diagonal_i = i + (numRows - row - 1) * 2
                    if diagonal_i < n:
                        zigzag_chars.append(s[diagonal_i])
            
        return "".join(zigzag_chars)

```


## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/61
    * 自分と同じく計算で行番号を決める方法と, 方向を管理してプロセスを模倣する方法の二つを挙げていた
* https://github.com/naoto-iwase/leetcode/pull/61
* https://github.com/mamo3gr/arai60/pull/55

# Step3

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        row_chars = [[] for _ in range(numRows)]
        row = 0
        direction = 1
        for ch in s:
            row_chars[row].append(ch)

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            
            row += direction
        
        result = []
        for ch_list in row_chars:
            result.extend(ch_list)
        
        return "".join(result)

```