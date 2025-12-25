## Node class contains value and next pointer
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

 ## LinkedList class with a constructor that initializes head, tail, and length       
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

 ## Creating an instance of LinkedList with initial value 4
my_linked_list = LinkedList(4)

## Displaying the head, tail, and length of the linked list
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    