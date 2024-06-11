class BitSet:
    def __init__(self, size):
        self.size = size
        self.bitset = [0] * ((size // 64) + 1)

    def add(self, index):
        self.bitset[index // 64] |= (1 << (index % 64))

    def contains(self, index):
        return (self.bitset[index // 64] & (1 << (index % 64))) != 0
