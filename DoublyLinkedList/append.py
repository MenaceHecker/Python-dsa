class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        if (self.length == 0):
            self.head = Node(value)
            self.tail = self.head
            self.next = None
            self.prev = None
            self.length += 1
            return True
        self.tail.next = Node(value)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.length += 1
        return True