# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        unique = dummy_head
        while unique.next:
            if unique.next.next is None:
                return dummy_head.next
            if unique.next.val != unique.next.next.val:
                unique = unique.next
                continue
            duplicated_val = unique.next.val
            unique_candidate = unique.next.next.next
            while unique_candidate is not None and unique_candidate.val == duplicated_val:
                unique_candidate = unique_candidate.next
            unique.next = unique_candidate
        return dummy_head.next
        