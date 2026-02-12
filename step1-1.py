class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_start = ListNode()
        dummy_start.next = head
        processed_end = dummy_start
        while processed_end is not None and processed_end.next is not None and processed_end.next.next is not None:
            if processed_end.next.val != processed_end.next.next.val:
                processed_end = processed_end.next
                continue
            delete_start = processed_end.next
            delete_end = processed_end.next.next
            while delete_end is not None and delete_start.val == delete_end.val:
                delete_end = delete_end.next
            processed_end.next = delete_end
        return dummy_start.next