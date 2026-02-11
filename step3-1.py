class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur is not None:
            if prev is not None and prev.val == cur.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head