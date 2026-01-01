def get(self, index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        for _ in range(index):
            temp = temp.next
        return temp

def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False