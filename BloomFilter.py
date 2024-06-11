from BitSet import BitSet
from HashFunctions import HashFunctions


class BloomFilter:
    def __init__(self, capacity, error_rate=0.01):
        self.size = self._best_m(capacity, error_rate)
        self.hash_function_count = self._best_k(capacity, error_rate)
        self.bitset = BitSet(self.size)
        self.get_hash_secondary = HashFunctions.hash_int32_shift

    def add(self, item):
        primary_hash = HashFunctions.hash_int32_jenkins(item)
        secondary_hash = self.get_hash_secondary(item)

        for i in range(1, self.hash_function_count + 1):
            combined_hash = (primary_hash + i * secondary_hash) % self.size
            self.bitset.add(combined_hash)

    def contains(self, item):
        primary_hash = HashFunctions.hash_int32_jenkins(item)
        secondary_hash = self.get_hash_secondary(item)

        for i in range(1, self.hash_function_count + 1):
            combined_hash = (primary_hash + i * secondary_hash) % self.size
            if not self.bitset.contains(combined_hash):
                return False
        return True

    @staticmethod
    def _best_m(capacity, error_rate):
        import math
        return int(-capacity * math.log(error_rate) / (math.log(2) ** 2))

    @staticmethod
    def _best_k(capacity, error_rate):
        import math
        return int((self._best_m(capacity, error_rate) / capacity) * math.log(2))

    @staticmethod
    def error_rate(capacity, size, hash_function_count):
        import math
        return (1 - math.exp(-hash_function_count * capacity / size)) ** hash_function_count
