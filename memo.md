# Step1

## アプローチ

* すべてのあり得るpermutationを出したい
* 候補集合があって、そこから１個とるのを候補集合がなくなるまで繰り返す
* O(N!)
    * 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720 
    * 720 / 10^6 ~= 7.0 * 10^-4 = 700 nsくらい

## Code1-1

* 7:48でAC
* とりあえず心配だからcopyを作ったり, 計算量を気にせずcandidatesをスライスでコピー生成している
* Step2で修正しよう

```python
import copy


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        def generate_permutations(candidates: list[int], permutations: list[list[int]]):
            if not candidates:
                return permutations

            result = []
            for i, candidate in enumerate(candidates):
                permutations_copy = copy.deepcopy(permutations)
                for permutation in permutations_copy:
                    permutation.append(candidate)
                result.extend(generate_permutations(candidates[:i] + candidates[i + 1:], permutations_copy))
            
            return result

        return generate_permutations(nums, [[]])

```


# Step2

## Code2-1

* 「今注目している候補以外でできるpermutationに候補を加える」という動作がわかりやすくなるようにした

```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        def generate_permutations(candidates: list[int]):
            if not candidates:
                return [[]]

            permutations = []
            for i, candidate in enumerate(candidates):
                permutations_without_candidate = generate_permutations(candidates[:i] + candidates[i + 1:])
                for permutation in permutations_without_candidate:
                    permutations.append(permutation + [candidate])

            return permutations

        return generate_permutations(nums)
            
```

## Code2-2

* whileを使ってもかけそうなので書いてみる
* バッチ的にpermutationsをまとめてstackに入れる方法と, 一つ一つのpermutationごとにstackに入れる方法がありそう
    * 今回は, デバッグのしやすさと解法の幅の観点から, 一つ一つのpermutationごとにstackに入れるようにした
    * 一つのpermutationごとに次に選ぶ候補を保存しておく

```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        result = []

        permutation_and_candidates = [([], nums)]
        while permutation_and_candidates:
            permutation, candidates = permutation_and_candidates.pop()

            if not candidates:
                result.append(permutation)
                continue

            for i in range(len(candidates)):
                permutation_and_candidates.append(
                    (permutation + [candidates[i]], candidates[:i] + candidates[i + 1:])
                )
        
        return result

```

# Step3

## 他の人のコードを見る

### olsen-blue: https://github.com/olsen-blue/Arai60/pull/51

* backtrackでは, 一つのpermutation引数を使い回す
* 最後の保存する際に, copyしたものを保存する

### naoto-iwase: https://github.com/naoto-iwase/leetcode/pull/51

* backtrackだと, スライスによるオーバーヘッドが乗らない分少しだけ計算量が緩和される

### mamo3gr: https://github.com/mamo3gr/arai60/pull/47

* 計算量はO(N!)ではなくて, O(N * N!)らしい
* copyをしているからか
    * 自分の実装は, O(N^2 * N!)
    *  N!個の配列が長さNでO(N * N!)かかる
    * 各再帰の段階でコピーをしているので, O(N)分余計にかかる


## 追加で実装

### Code3-3 (BackTrack)

* 無駄な配列のコピー(candidateのコピー)がないのでO(N * N!)になった

```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        all_permutations = []

        permutation = []
        used_indices = set()
        def generate_permutations() -> None:
            if len(permutation) == len(nums):
                all_permutations.append(permutation.copy())
                return

            for i in range(len(nums)):
                if i in used_indices:
                    continue
                used_indices.add(i)
                permutation.append(nums[i])
                generate_permutations()
                permutation.pop()
                used_indices.remove(i)
            return
        
        generate_permutations()
        return all_permutations
                
```

# Step4

```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        all_permutations = []
        permutation = []
        used_indices = set()
        def generate_permutations():
            if len(permutation) == len(nums):
                all_permutations.append(permutation.copy())
                return 
            
            for i in range(len(nums)):
                if i in used_indices:
                    continue

                used_indices.add(i)
                permutation.append(nums[i])

                generate_permutations()

                used_indices.remove(i)
                permutation.pop()
            
            return 
        
        generate_permutations()
        return all_permutations
        

```
