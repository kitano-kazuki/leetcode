class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        delete_start = head
        delete_end = head.next
        while delete_end is not None and delete_end.val == delete_start.val:
            delete_end = delete_end.next
        return self.deleteDuplicates(delete_end)
        