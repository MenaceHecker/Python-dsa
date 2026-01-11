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
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if index > self.length//2:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            temp.prev.next = new_node
            new_node.prev = temp.prev
            new_node.next = temp
            temp.prev = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            if temp.next:
                temp.next.prev = new_node
            temp.next = new_node
        self.length += 1
        return True