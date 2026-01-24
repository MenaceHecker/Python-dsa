def get_item(self, key):
    index = self.__hash(key)
    if self.data_map[index] is not None:
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                ## Found the key, return the value since this is a key-value store
                return self.data_map[index][i][1]
    return None