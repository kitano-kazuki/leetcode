# Step1

* 今日からC++でやってみる

## アプローチ

* [name, email1, email2, ...]がたくさん与えられる. それらのうち, 共通するemailを持つものをマージする(このときnameは必ず一致するとする)
* 名前が一緒のものたちをグルーピング
* それら一つずつ, 同名の他のアカウントと共通するemailがないかを確認する
* 最悪の場合は, 全員が同じ名前で、それぞれのアカウントのemailがたくさんある場合
    * O(L * N^2)
    * 実行時間: 10^6 * 10 / 10^7 ~= 1secくらい
    * C++なら1秒程度で終わりそう。。。?
* UnionFindで最終的に一つのデカグループごとにまとめられると嬉しい
* ここまで11:21

## Code1-1

* `unordered_map`とか`set`とかをリファレンス見ながら頑張って書いた
* `iterator`の扱いが難しい
    * `iter->second.push_back`とかにするのがややこしい

```cpp

#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <algorithm>

using namespace std;

class UnionFind {
private:
  vector<int> parents;
  vector<int> sizes;

public:
  UnionFind(int n) : parents(n), sizes(n, 1){
    for (int i = 0; i < n; i++){
      parents[i] = i;
    }
  }

  int find(int p){
    if (parents[p] == p){
      return p;
    }
    int parent = find(parents[p]);
    parents[p] = parent;
    return parent;
  }

  void unite(int p1, int p2){
    int parent1 = find(p1);
    int parent2 = find(p2);
    if (parent1 == parent2){
      return;
    }
    if (sizes[parent1] < sizes[parent2]){
      parents[parent1] = parent2;
      sizes[parent2] += sizes[parent1];
      return;
    } else {
      parents[parent2] = parent1;
      sizes[parent1] += sizes[parent2];
      return;
    }
  }

  vector<vector<int>> group_parents(){
    using mymap = unordered_map<int, vector<int>>;
    mymap parent_to_children;
    for (int i = 0; i < parents.size(); i++){
      int parent = find(i);
      auto iter = parent_to_children.try_emplace(parent).first;
      iter->second.push_back(i);
    }

    vector<vector<int>> groups;
    for_each(
        parent_to_children.begin(),
        parent_to_children.end(),
        [&](mymap::value_type p){groups.push_back(p.second);}
    );

    return groups;
  }

};


class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
      unordered_map<string, vector<int>>  name_to_ids;
      unordered_map<int, set<string>> id_to_emails;
      for (int i = 0; i < accounts.size(); i++){
        string name = accounts[i][0];
        auto iter = name_to_ids.try_emplace(name).first;
        iter->second.push_back(i);

        id_to_emails.try_emplace(i, accounts[i].begin() + 1, accounts[i].end());
      }

      UnionFind uf(accounts.size());
      for (int id1 = 0; id1 < accounts.size(); id1++){
        for (int id2 = id1 + 1; id2 < accounts.size(); id2++){
          if (!is_same_account(id1, id2, id_to_emails)){
            continue;
          }
          uf.unite(id1, id2);
        }
      }

      vector<vector<string>> result;
      vector<vector<int>> groups = uf.group_parents();
      for (vector<int>& group : groups){
        vector<string> emails = unite_emails(group, id_to_emails);
        vector<string> account{accounts[group[0]][0]};
        account.insert(account.end(), emails.begin(), emails.end());
        result.push_back(account);
      }

      return result;
    }

private:
    template <class T>
    int has_common(const set<T>& s1, const set<T>& s2){
      const set<T>* small;
      const set<T>* large;
      if (s1.size() <= s2.size()){
        small = &s1;
        large = &s2;
      } else {
        small = &s2;
        large = &s1;
      }

      for (const T& e : *small){
        if (large->count(e)){
          return true;
        }
      }

      return false;
    }

    bool is_same_account(int id1, int id2, const unordered_map<int, set<string>>& id_to_emails){
      const set<string>& emails1 = id_to_emails.find(id1)->second;
      const set<string>& emails2 = id_to_emails.find(id2)->second;
      return has_common(emails1, emails2);
    }

    vector<string> unite_emails(const vector<int>& ids, const unordered_map<int, set<string>>& id_to_emails){
      set<string> united_emails;
      for (int id : ids){
        const set<string>& emails = id_to_emails.find(id)->second;
        for (string email : emails){
          united_emails.insert(email);
        }
      }
      return vector<string>(united_emails.begin(), united_emails.end());
    }


};

```

# Step2

## 他の人のPRを見る

* https://github.com/tom4649/Coding/pull/108
* https://github.com/huyfififi/coding-challenges/pull/48
    * union-findの解法
        * メール->accountsのインデックス`i`を保存するmapを用意
        * accountsの`j`のメールに対するmapのエントリ(メール->`i`)がすでにある場合
            * `j`と`i`が同じアカウントを表すとしてunionする
        * `unionfind`の親->メールアドレス群を用意
        * 上記をsetにして完成
    * DFSの解法
        * accountごとに最初のメアドをハブとして, 他のメアドに対してエッジを繋ぐ
        * 同一のメアドが別のaccountで出た時は, あらたにエッジが作られることになる
            * 少なくともハブを経由すれば同一のメアドを持つ別のアカウントの他のメアド全てにパスが存在
        * 一回のtraverseで訪れることのできるメアドが, マージ後のメアドになる

## Code2-2 (DFS)

```cpp
#include <vector>
#include <unordered_map>
#include <set>
#include <stack>
#include <algorithm>

using namespace std;


class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
      // 辺を構築
      unordered_map<string, vector<string>> email_to_neighbors;
      unordered_map<string, string> hub_to_name;
      for (const vector<string>& account : accounts){
        const string& name = account[0];
        const string& hub_email = account[1];

        if (hub_to_name.find(hub_email) == hub_to_name.end()){
          hub_to_name.emplace(hub_email, name);
        }

        vector<string>& hub_neighbors = email_to_neighbors.try_emplace(hub_email).first->second;
        for (auto iter = account.begin() + 2; iter != account.end(); iter++){
          const string& email = *iter;

          // hub -> email
          hub_neighbors.push_back(email);

          // email -> hub
          auto map_iter = email_to_neighbors.try_emplace(email).first;
          vector<string>& neighbors = map_iter->second;
          neighbors.push_back(hub_email);
        }
      }

      // DFS
      vector<vector<string>> merged_accounts;
      set<string> visited;
      for (auto iter = hub_to_name.begin(); iter != hub_to_name.end(); iter++){
        const string& hub = iter->first;
        if (visited.find(hub) != visited.end()){
          continue;
        }
        const string& name = iter->second;
        vector<string> merged_account{name};
        traverse(hub, merged_account, visited, email_to_neighbors);
        sort(merged_account.begin() + 1, merged_account.end());
        merged_account.erase(unique(merged_account.begin() + 1, merged_account.end()), merged_account.end());
        merged_accounts.push_back(merged_account);
      }

      return merged_accounts;
    }


    void traverse(const string& start_email, vector<string>& merged_account, set<string>& visited, const unordered_map<string, vector<string>>& email_to_neighbors){
      stack<string> emails_to_visit;
      emails_to_visit.push(start_email);

      while (!emails_to_visit.empty()){
        const string email = emails_to_visit.top();
        emails_to_visit.pop();
        merged_account.push_back(email);
        visited.insert(email);

        const vector<string>& neighbors = email_to_neighbors.find(email)->second;
        for (const string& neighbor_email : neighbors){
          if (visited.find(neighbor_email) != visited.end()){
            continue;
          }
          emails_to_visit.push(neighbor_email);
        }
      }
    }


};

```


# Step3

## Code3-2 (DFS)

* C++は慣れてないのもあってめっちゃ時間がかかる...

* 1st: 31:08
* 2nd: 12:45
* 3rd: 9:50

```cpp
#include <unordered_map>
#include <set>
#include <algorithm>
#include <vector>
#include <stack>


using namespace std;


class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
      // ----辺を構築----
      // hubはaccountに最初に登録されたメアド
      unordered_map<string, string> hub_to_name;
      unordered_map<string, vector<string>> email_to_neighbors;
      for (vector<string>& account : accounts){
        string& name = account[0];
        string& hub = account[1];
        hub_to_name.try_emplace(hub, name);

        vector<string>& hub_neighbors = email_to_neighbors.try_emplace(hub).first->second;
        for (auto iter = account.begin() + 2; iter != account.end(); iter++){
          string email = *iter;
          hub_neighbors.push_back(email);
          vector<string>& email_neighbors = email_to_neighbors.try_emplace(email).first->second;
          email_neighbors.push_back(hub);
        }
      }

      // ----DFS----
      vector<vector<string>> merged_accounts;
      set<string> visited;
      for (auto iter = hub_to_name.begin(); iter != hub_to_name.end(); iter++){
        string hub = iter->first;
        if (visited.find(hub) != visited.end()){
          continue;
        }
        string name = iter->second;
        vector<string> merged_account{name};
        traverse(hub, merged_account, visited, email_to_neighbors);
        sort(merged_account.begin() + 1, merged_account.end());
        merged_account.erase(unique(merged_account.begin() + 1, merged_account.end()), merged_account.end());

        merged_accounts.push_back(merged_account);
      }

      return merged_accounts;
    }


    void traverse(string start_email, vector<string>& merged_account, set<string>& visited, unordered_map<string, vector<string>> email_to_neighbors){
      stack<string> emails_to_visit;
      emails_to_visit.push(start_email);

      while (!emails_to_visit.empty()){
        string email = emails_to_visit.top();
        emails_to_visit.pop();
        merged_account.push_back(email);
        visited.insert(email);

        const vector<string>& neighbors = email_to_neighbors.find(email)->second;
        for (string neighbor_email : neighbors){
          if (visited.find(neighbor_email) != visited.end()){
            continue;
          }
          emails_to_visit.push(neighbor_email);
        }
      }
    }
};

```
