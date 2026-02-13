class Solution:
    def parseListAsInteger(self, l):
        node = l
        digits = []
        while node is not None:
            digits.append(node.val)
            node = node.next
        digits = digits[::-1]
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        return num

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.parseListAsInteger(l1)
        num2 = self.parseListAsInteger(l2)
        summed_num = num1 + num2
        if summed_num == 0:
            return ListNode(0)
        dummy_head = ListNode(0)
        node = dummy_head
        while summed_num > 0:
            digit_node = ListNode(summed_num % 10)
            node.next = digit_node
            node = node.next
            summed_num = summed_num // 10
        return dummy_head.next
            
        