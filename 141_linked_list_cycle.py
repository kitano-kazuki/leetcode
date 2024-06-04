from typing import Optional

# Definition for singly-linked list.
class ListNode:
 def __init__(self, x):
     self.val = x
     self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        visited = []
        i = 0
        target = head
        while target.next is not None:
            target = target.next
            if target in visited:
                return True
            else:
                visited.append(target)
        return False


head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
solution = Solution()
result = solution.hasCycle(head)
print(result)
