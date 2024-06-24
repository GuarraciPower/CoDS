from BitSet import BitSet
from HashFunctions import HashFunctions


class BloomFilter:
    def __init__(self, capacity, error_rate=0.01, hash_function='jenkins'):
        self.size = self._best_m(capacity, error_rate)
        self.hash_function_count = self._best_k(capacity, error_rate)
        self.bitset = BitSet(self.size)

        # Select primary and secondary hash functions
        if hash_function == 'murmur':
            self.get_hash_primary = HashFunctions.hash_murmur
            self.get_hash_secondary = HashFunctions.hash_murmur
        elif hash_function == 'city':
            self.get_hash_primary = HashFunctions.hash_city
            self.get_hash_secondary = HashFunctions.hash_city
        elif hash_function == 'sha256':
            self.get_hash_primary = HashFunctions.hash_sha256
            self.get_hash_secondary = HashFunctions.hash_sha256
        else:  # default to jenkins
            self.get_hash_primary = HashFunctions.hash_int32_jenkins
            self.get_hash_secondary = HashFunctions.hash_int32_shift

    def add(self, item):
        item_hash = HashFunctions.hash_string(item)
        item_hash_bytes = str(item_hash).encode('utf-8')
        primary_hash = self.get_hash_primary(item_hash_bytes)
        secondary_hash = self.get_hash_secondary(item_hash_bytes)

        print("Primary Hash:", primary_hash, "Secondary Hash:", secondary_hash)

        if primary_hash is None or secondary_hash is None:
            raise ValueError("Hash functions returned None")

        for i in range(1, self.hash_function_count + 1):
            combined_hash = (primary_hash + i * secondary_hash) % self.size
            self.bitset.add(combined_hash)

    def contains(self, item):
        item_hash = HashFunctions.hash_string(item)
        item_hash_bytes = str(item_hash).encode('utf-8')
        primary_hash = self.get_hash_primary(item_hash_bytes)
        secondary_hash = self.get_hash_secondary(item_hash_bytes)

        if primary_hash is None or secondary_hash is None:
            return False

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
        return int((BloomFilter._best_m(capacity, error_rate) / capacity) * math.log(2))

    @staticmethod
    def error_rate(capacity, size, hash_function_count):
        import math
        return (1 - math.exp(-hash_function_count * capacity / size)) ** hash_function_count
