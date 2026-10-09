## Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        prev = dummy
        c1 = head
        c2 = head

        for _ in range(n):
            c2 = c2.next

        while c2 is not None:
            prev = c1
            c1 = c1.next
            c2 = c2.next

        prev.next = c1.next
        c1.next = None

        return dummy.next