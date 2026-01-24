def set_item(self, key, value):
    """Set the value associated with key in the set.

    Since this is a set, the value is ignored and only the key is stored.

    Args:
        key: The key to add to the set.
        value: Ignored.
    """
    index = self.__hash(key)
    if self.data[index] == None:
        self.data[index] = []
    # Check if the key already exists and update it
    self.data[index].append([key, value])