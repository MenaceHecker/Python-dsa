## Given the head of a singly linked list, reverse the list, and return the reversed list.

## Recursive solution
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        new_node = ListNode()
        self.head = new_node
        self.length = 1
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

            

      



        