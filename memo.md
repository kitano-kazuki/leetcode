# Step1

## アプローチ

* 与えられた配列から値を選んで合計がぴったりtargetになる組み合わせを出力する
* 最初に思いついたのはDP
    * targetを作るためには, target - numが作れれば良くて,...
        * targetを作れるかどうかの判定には使えるかけど, 具体的な組み合わせを出すことはできない？？
        * target - numを作るのに何を使ったかを記録しておけばできるかも
* 次に思いつくのは, すべての列挙を行う
    * targetに達するまで値を採用したりしなかったりしたパターンを出す
    * でも, 同じ値を何回でも使っていいせいでパターン数が膨大になるかも
    * 仮に同じ値を1回しか使ってはいけないとしても, 全パターンを出していたら2^30パターン見る必要があるな
* DP的(あるいは再帰)にやるのがよさそう
* 作りたい値がtargetの最大値種類: M
* それぞれの作りたい値ごとにcandidateの要素数N分調べる
* 全体の計算量は O(M * N) 
* 計算にかかる時間は, 40 * 30 / 10^6 ~= 1.2 * 10^-3 = 12 ms

## Code1-1

* 重複（順番違い）を消すために別のコードを用意している
* もっと効率の良い方法があったら嬉しいのでstep2で模索する

```python
import functools


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        @functools.cache
        def combination_sum_helper(target: int) -> list[list[int]]:
            if target < 0:
                return []

            if target == 0:
                return [[]]

            all_combinations = []
            for candidate in candidates:
                combinations = combination_sum_helper(target - candidate)
                if not combinations:
                    continue
                all_combinations.extend([combination + [candidate] for combination in combinations])
            
            return all_combinations

        combinations_with_duplicates = sorted([sorted(combination) for combination in combination_sum_helper(target)])
        previous_combination = None
        unique_combinations = []
        for combination in combinations_with_duplicates:
            if previous_combination is not None and previous_combination == combination:
                continue
            unique_combinations.append(combination)
            previous_combination = combination

        return unique_combinations
            

```            

# Step2

## Code2-1

* tupleならハッシュ可能になるので, tuple()を使用

```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        completed_combinations = set()
        all_combinations = []
        def generate_combination_sum(target: int, combination: list[int]) -> None:
            if target < 0:
                return
            if target == 0:
                combination_tuple = tuple(sorted(combination))
                if combination_tuple in completed_combinations:
                    return
                all_combinations.append(combination.copy())
                completed_combinations.add(combination_tuple)
                return

            for candidate in candidates:
                combination.append(candidate)
                generate_combination_sum(target - candidate, combination)
                combination.pop()
            
            return
        
        generate_combination_sum(target, [])
        return all_combinations

``` 
            
# Step3

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/53
    * 前問のすべてのsubsetを出す問題のように, 前から順番にインデックスを進めながら行うbacktrackなら重複の処理は不要.
        * 自分がこの解法をなぜ避けたかというと, 同じ値を何回でも使っていいせいでパターンが膨大になると思ったから
            * でも, 自分の方法でも計算量は結局よくなってない.
        * targetの値がたかだか40なので, 和が40を超えたパターンは棄却していい
        * target=Mのときにそのパターン数を出すための計算量をT(M)とする
        * T(M) = T(M - x1) + T(M - x2) + .. + T(M - xn)
        * T(M) = n * T(M - x) (ざっくりxはMより少し小さいtargetを計算するために引いている数とする)
        * T(M) = n^M (上界を考えるならMが1ずつ減る時を考えればいい. 今回はcandidateの最小値が2だからM//2でもいいけど, 一般化したいからcandidateの最小値が1とする)
        * step数は, 30^40 ~= 10^50くらい？？
            * さすがに上界としてガバガバすぎる気もする
        * 問題の制約target is less than 150に助けられているだけかな
        * https://github.com/Mike0121/LeetCode/pull/1#discussion_r1578212926
            * > 答えの数ですが、candidates = [1..target] の場合、これは分割数というものですね。
        * https://discord.com/channels/1084280443945353267/1233295449985650688/1242103186009886862
            * > いやー、分割数の極限での振る舞いを聞いて、いまのところ答えられた人は一人です。
        * https://github.com/naoto-iwase/leetcode/pull/53/files#r2535863967
            * > 分割数の極限の話は普通知らない上に、かなりややこしいです。撤退していいと思います。


# Step4

## Code4-2 (Backtrack)

```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        all_combinations = []

        def generate_combinations(index: int, sum_in_combination: int, combination: list[int]) -> None:
            if sum_in_combination > target:
                return
            if sum_in_combination == target:
                all_combinations.append(combination.copy())
                return
            if index == len(candidates):
                return
            
            combination.append(candidates[index])
            generate_combinations(index, sum_in_combination + candidates[index], combination)
            combination.pop()

            generate_combinations(index + 1, sum_in_combination, combination)

            return
        
        generate_combinations(0, 0, [])
        return all_combinations

```