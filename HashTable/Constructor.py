class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        hash_index = 0
        for char in key:
            hash_index = (hash_index + ord(char) * 23) % len(self.data_map)
        return hash_index