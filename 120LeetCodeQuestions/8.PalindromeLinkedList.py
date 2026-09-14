## Given the head of a singly linked list, 
## return true if it is a palindrome or false otherwise.

## Implemented with list approach
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        arr = []
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        return arr == arr[::-1]