## Initilizing Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
## Initilizing LinkedList class
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
 ## Appending new node to the end of the linked list       
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        ## If the list is empty, return None
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        ## Traverse to the end of the list
        while(temp.next):
            pre = temp
            temp = temp.next
        ## Update tail to the second last node
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        ## If the list becomes empty after pop, set head and tail to None
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

 


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""