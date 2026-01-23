class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        my_hash = 0
        for char in key:
            my_hash = (my_hash + ord(char) * 23) % len(self.data_map)
        return my_hash