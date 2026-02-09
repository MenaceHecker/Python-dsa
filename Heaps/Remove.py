    def remove(self):
    if len(self.head) == 0:
        return None

    if len(self.head) == 1:
        return self.head.pop()

    max_value = self.head[0]
    self.head[0] = self.head.pop()
    self.sink_down(0)

    return max_value
     