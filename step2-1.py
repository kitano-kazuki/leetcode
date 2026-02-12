class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_start = ListNode()
        dummy_start.next = head
        unique = dummy_start
        while unique.next is not None:
            unique_candidate = unique.next
            if unique_candidate.next is None or unique_candidate.val != unique_candidate.next.val:
                unique = unique.next
            else:
                duplication_val = unique_candidate.val
                while unique_candidate is not None and unique_candidate.val == duplication_val:
                    unique_candidate = unique_candidate.next
                unique.next = unique_candidate
        return dummy_start.next