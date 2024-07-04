#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *reverseList(ListNode *head) {
    if (head == nullptr || head->next == nullptr) {
      return head;
    }
    ListNode *before = head;
    ListNode* nxt = head->next;
    head->next = nullptr;
    head = nxt;
    while (head != nullptr) {
      nxt = head->next;
      head->next = before;
      before = head;
      head = nxt;
    }
    return before;
  }
};
