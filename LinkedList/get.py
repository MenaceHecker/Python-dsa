def get(self, index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        for _ in range(index):
            temp = temp.next
        return temp