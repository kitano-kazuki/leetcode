class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur is not None:
            if prev is not None and prev.val == cur.val:
                to_delete = cur
                prev.next = cur.next
                cur = prev.next
                del to_delete
            else:
                prev = cur
                cur = cur.next
        return head