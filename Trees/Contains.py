def contains(self, value):
        node_to_check = Node(value)
        temp = self.root
        if temp is None:
            return False
        while temp is not None:
            if node_to_check.value < temp.value:
                temp = temp.left
            elif node_to_check.value > temp.value:
                temp = temp.right
            elif node_to_check.value == temp.value:
                return True
        return False