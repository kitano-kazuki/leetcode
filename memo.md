# Step1

## アプローチ

* `numCourses`個のコースを全部取り切れるか判定する. 
* `prerequisites[i] = [a_i, b_i]`は, コース`a_i`を取るためには, 先にコース`b_i`をとらなければいけないことを意味する
* 全てのコースを取れる場合は`True`そうではない場合は`False`を返す関数を作る
* トポロジカルソート
* 各コースごとに, 先に取らなければいけないコースの数を記録しておく
* 先に取らなければいけないコースの個数が0だったら, そのコースを取る
* コースをとった後, そのコースが条件となっていたコースの先に取らなければいけないコース数を1減らす.
    * その結果先に取らなければいけないコース数が0になったら, 取れるコース一覧に追加する
* まだとっていないコースが残っていなければOK
* O(N^2)かな?
    * `N`個のコースごとに, 依存するコースの取らなければいけないコース数を更新
    * 2000^2 / 10^6 ~= 2secくらい
* 5:28

## Code1-1

* AC: 5:27

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        num_pretake = [0] * numCourses
        posttakes = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            num_pretake[a] += 1
            posttakes[b].append(a)

        courses_takable = [i for i in range(numCourses) if num_pretake[i] == 0]

        taken_count = 0
        while courses_takable:
            course = courses_takable.pop()
            taken_count += 1
            for dependent in posttakes[course]:
                num_pretake[dependent] -= 1
                if num_pretake[dependent] == 0:
                    courses_takable.append(dependent)
        
        return taken_count == numCourses

        
```

# Step2

## Code2-1

* トポロジカルソートの計算量は, 辺を１回ずつ見るので, O(V + E)
* Eは最悪の場合N^2程度になるとして見積もれるので, O(N^2)ではあるか

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        num_pretake = [0] * numCourses
        dependents = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            num_pretake[a] += 1
            dependents[b].append(a)

        courses_takable = [i for i in range(numCourses) if num_pretake[i] == 0]

        taken_count = 0
        while courses_takable:
            course = courses_takable.pop()
            taken_count += 1
            for dependent in dependents[course]:
                num_pretake[dependent] -= 1
                if num_pretake[dependent] == 0:
                    courses_takable.append(dependent)
        
        return taken_count == numCourses
        
```

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/34
    * 自分の解放（トポロジカルソート）とは別に, グラフにサイクルがあるかどうかで判定する方法も考えていた

## Code2-2 (Detect Cycle)

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependents = [[] for _ in range(numCourses)]
        for dependent, course in prerequisites:
            dependents[course].append(dependent)


        has_cycle = [None] * numCourses
        courses_in_path = set()
        def detect_cycle(course: int) -> bool:
            if has_cycle[course] is not None:
                return has_cycle[course]

            if course in courses_in_path:
                has_cycle[course] = True
                return True

            courses_in_path.add(course)
            for dependent in dependents[course]:
                if detect_cycle(dependent):
                    has_cycle[course] = True
                    return True

            courses_in_path.remove(course)
            has_cycle[course] = False
            return False

        for i in range(numCourses):
            if detect_cycle(i):
                return False

        return True
        
```

# Step3

## Code3-1

* 3:38
* 2:15
* 2:00

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependents = [[] for _ in range(numCourses)]
        num_pretake = [0] * numCourses
        for dependent, course in prerequisites:
            dependents[course].append(dependent)
            num_pretake[dependent] += 1
        
        courses_takable = []
        for i in range(numCourses):
            if num_pretake[i] == 0:
                courses_takable.append(i)
        
        num_taken = 0
        while courses_takable:
            course = courses_takable.pop()
            num_taken += 1
            for dependent in dependents[course]:
                num_pretake[dependent] -= 1
                if num_pretake[dependent] == 0:
                    courses_takable.append(dependent)
        
        return num_taken == numCourses

        
```
