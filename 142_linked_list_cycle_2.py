from typing import Optional

# Definition for singly-linked list.
class ListNode:
 def __init__(self, x):
     self.val = x
     self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        visited = [head]
        target = head
        while target.next is not None:
            target = target.next
            if target in visited:
                return target
            else:
                visited.append(target)
        return None


head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
solution = Solution()
result = solution.detectCycle(head)
print(result)
