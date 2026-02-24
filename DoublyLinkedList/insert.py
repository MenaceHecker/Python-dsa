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
    
    # def insert(self, index, value):
    #     new_node = Node(value)
    #     if index < 0 or index > self.length:
    #         return False
    #     if index > self.length//2:
    #         temp = self.tail
    #         for _ in range(self.length - 1, index, -1):
    #             temp = temp.prev
    #         temp.prev.next = new_node
    #         new_node.prev = temp.prev
    #         new_node.next = temp
    #         temp.prev = new_node
    #     else:
    #         temp = self.head
    #         for _ in range(index - 1):
    #             temp = temp.next
    #         new_node.next = temp.next
    #         new_node.prev = temp
    #         if temp.next:
    #             temp.next.prev = new_node
    #         temp.next = new_node
    #     self.length += 1
    #     return True

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True
    
    