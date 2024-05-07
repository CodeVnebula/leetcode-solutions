"""
    You are given the head of a non-empty linked list representing a non-negative 
    integer without leading zeroes.

    Return the head of the linked list after doubling it.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head):
        # Reversing
        prev, current = None, head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Working on reversed linked list
        carry = 0
        current = prev 
        while current:
            double_value = current.val * 2 + carry
            current.val = double_value % 10 
            carry = double_value // 10        
            if not current.next and carry > 0:
                current.next = ListNode(carry)
                break
            current = current.next
        
        # Reversing again
        prev, current = None, prev
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev  # New head
