#include <iostream>
#include <vector>

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  // NOTE: Fail when a duplicate number appears in the first place

  // ListNode *deleteDuplicates(ListNode *head) {
  //   ListNode *prev = head;
  //   ListNode *cur = head->next;
  //   while (cur != nullptr) {
  //     if (cur->next == nullptr) {
  //       break;
  //     }
  //     if (cur->val == cur->next->val) {
  //       ListNode *arrow = cur->next;
  //       while (cur->val == arrow->val) {
  //         if(arrow == nullptr){
  //           prev->next = nullptr;
  //           return head;
  //         }
  //         arrow = arrow->next;
  //       }
  //       prev->next = arrow;
  //       cur = arrow;
  //     } else {
  //       prev = cur;
  //       cur = cur->next;
  //     }
  //   }
  //   return head;
  // }

  ListNode *deleteDuplicates(ListNode *head) {
    ListNode dummy(0, head);
    ListNode *prev = &dummy;
    ListNode *cur = head;
    while (cur) {
      ListNode *nextNode = cur->next;
      while (nextNode && cur->val == nextNode->val) {
        nextNode = nextNode->next;
      }

      if (cur->next == nextNode) {
        prev = cur;
      } else {
        prev->next = nextNode;
      }
      cur = nextNode;
    }
    return dummy.next;
  }
};
