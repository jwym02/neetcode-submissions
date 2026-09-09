# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
            for each node in both linked lists, add both nodes together to get a variable called total.
            total // 10 to get the carry_over and total % 10 to get the remainder.
            remainder will stay as curr.val, and when we move on to the next node, add the values and carry_over together
            condition of while loop will be while l1 or l2 or carry
        """

        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            remainder = total % 10

            curr.next = ListNode(remainder) # create a new node & attach it
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummy.next