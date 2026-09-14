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


## Implementation with stack approach
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        # Store all node values in the stack
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next

        # Compare linked-list values with reversed stack values
        curr = head
        while curr:
            if curr.val != stack.pop():
                return False

            curr = curr.next

        return True

### Implementation with pointer approach
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        # Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Skip the middle node for odd-length lists
        if fast:
            slow = slow.next

        # Reverse the second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Compare the two halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True