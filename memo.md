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


