# Step1

## アプローチ

* `A~Z`のいづれかのラベルがついたタスクと, `n`が与えられる.
* CPUは1cycleごとに1つのタスクを実行する.
* ただし, 同じラベルがついたtaskを再び実行するまでには`n`サイクル開けなければいけない.
* 各タスクごとに待ち時間を保存しておく.
* 待ち時間が0のもののうち, 残りタスク数が多いものから処理をしていく.
* 実行可能なタスク集合は, 残りタスク数をもとにしたmax-heap
* クールダウン中のタスク集合は, タスク->残り待ち時間のunordered_map
* サイクルごとに, 実行可能集合から一つ取り出して実行. クールダウン集合の待ち時間を1減らす. 0になったものがあったら, 実行可能集合のheapに挿入.
* 計算量
    * `tasks.size() = M`とする
    * `n = N`とする
    * O(M * N)
    * 実行時間: 10^4 * 10^2 / 10^7 ~= 0.1 sec

## Code1-1

```cpp
#include <unordered_map>
#include <vector>
#include <queue>



class Solution {
public:
    int leastInterval(std::vector<char>& tasks, int n) {

      std::unordered_map<char, int> label_to_num_tasks;
      for (char task_label : tasks) {
        label_to_num_tasks[task_label]++;
      }

      std::priority_queue<std::pair<int, char>> executables;
      for (const auto& [label, num_tasks] : label_to_num_tasks) {
        executables.push({num_tasks, label});
      }
      std::vector<int> waitings(26);

      int num_remaining_tasks = tasks.size();
      int cycle = 0;
      while (num_remaining_tasks > 0) {
        cycle++;
        for (int c = 'A'; c <= 'Z'; c++) {
          if (waitings[c - 'A'] == 0) {
            continue;
          }
          waitings[c - 'A']--;
          if (waitings[c - 'A'] == 0) {
            int num_tasks = label_to_num_tasks[c];
            if (num_tasks > 0) {
              executables.push({num_tasks, c});
            }
          }
        }

        if (!executables.empty()) {
          auto [num_tasks, label] = executables.top();
          executables.pop();
          label_to_num_tasks[label]--;
          num_remaining_tasks--;
          waitings[label - 'A'] = n + 1;
        }
      }

      return cycle;
    }
};

```

# Step2

## LeetCodeの解法を見る

* 解法2 (cycle)
    * `n + 1`サイクルの間は制約を気にすることなく, タスクを割り当てることができる.
    * サイクルごとに残っているタスクの個数が多いラベル順に処理を行う
* 解法3
    * タスクの個数が一番大きいラベルを最初に割り当てると, 間に空のスロットができる.
    * そこに残りのタスクを割り当てることで, 余った空のスロット(=idle状態になる)の個数がわかる

## Code2-2 (Cycle)

```cpp
#include <queue>
#include <vector>


class Solution {
public:
    int leastInterval(std::vector<char>& tasks, int n) {
      std::vector<int> frequencies(26);
      for (char task : tasks) {
        frequencies[task - 'A']++;
      }
      std::priority_queue<int> remaining_frequencies;
      for (int i = 0; i < 26; i++) {
        if (frequencies[i] == 0) {
          continue;
        }
        remaining_frequencies.push(frequencies[i]);
      }

      int time = 0;
      int cycle = n + 1;
      while (true) {
        int time_in_cycle = 0;
        int num_task_done_in_cycle = 0;
        std::vector<int> next_frequencies;
        while (time_in_cycle < cycle && !remaining_frequencies.empty()) {
          int frequency = remaining_frequencies.top();
          remaining_frequencies.pop();
          num_task_done_in_cycle++;
          if (frequency - 1 > 0) {
            next_frequencies.push_back(frequency - 1);
          }
          time_in_cycle++;
        }
        for (int frequency : next_frequencies) {
          remaining_frequencies.push(frequency);
        }
        if (!remaining_frequencies.empty()) {
          time += cycle;
          continue;
        } else {
          time += num_task_done_in_cycle;
          return time;
        }
      }
    }
};

```

## Code2-3 (Calculate empty slots)

```cpp
#include <queue>
#include <vector>


class Solution {
public:
    int leastInterval(std::vector<char>& tasks, int n) {
      std::vector<int> frequencies(26);
      int max_frequency = 0;
      int max_count = 0;
      for (char task : tasks) {
        frequencies[task - 'A']++;
        if (frequencies[task - 'A'] == max_frequency) {
          max_count++;
          continue;
        }
        if (frequencies[task - 'A'] > max_frequency) {
          max_frequency = frequencies[task - 'A'];
          max_count = 1;
          continue;
        }
      }

      int num_parts = max_frequency - 1;
      int num_empty_slots = std::max(0, num_parts * (n - (max_count - 1)));

      int num_all_tasks = tasks.size();
      int num_remaining_tasks = num_all_tasks - max_frequency * max_count;

      return num_all_tasks + std::max(0, num_empty_slots - num_remaining_tasks);
    }
};

```

# Step3

## Code3-2 (Cycle)

```cpp
#include <queue>
#include <vector>


class Solution {
public:
    int leastInterval(std::vector<char>& tasks, int n) {
      std::vector<int> frequencies(26);
      for (char task : tasks) {
        frequencies[task - 'A']++;
      }

      std::priority_queue<int> remaining_frequencies;
      for (int i = 0; i < 26; i++) {
        if (frequencies[i] == 0) {
          continue;
        }
        remaining_frequencies.push(frequencies[i]);
      }

      const int cycle = n + 1;
      int time = 0;
      while (true) {
        int time_in_cycle = 0;
        int num_tasks_done = 0;
        std::vector<int> frequencies_in_next_cycle;
        while (time_in_cycle < cycle && !remaining_frequencies.empty()) {
          int frequency = remaining_frequencies.top();
          remaining_frequencies.pop();
          if (frequency - 1 > 0) {
            frequencies_in_next_cycle.push_back(frequency - 1);
          }

          num_tasks_done++;
          time_in_cycle++;
        }

        for (int frequency : frequencies_in_next_cycle) {
          remaining_frequencies.push(frequency);
        }

        if (!remaining_frequencies.empty()) {
          time += cycle;
          continue;
        } else {
          time += num_tasks_done;
          return time;
        }
      }

    }
};

```
