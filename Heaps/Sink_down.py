def _sink_down(self, index):
    max_index = index
    while True:
        left_index = self._left_child(index)
        right_index = self._right_child(index)
        if ( left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
            max_index = left_index

        if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
            max_index = right_index

        if max_index != index:
            self._swap(index, max_index)
            index = max_index
        else:
            return
        