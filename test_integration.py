import unittest
from test_bloom_filter import BloomFilter
from test_BitSet import BitSet
from test_HashFunctions import HashFunctions

class TestIntegration(unittest.TestCase):
    def test_bloom_filter_with_bitset_and_hash_functions(self):
        capacity = 10 ** 5
        error_rate = 0.01
        bf = BloomFilter(capacity, error_rate, hash_function='murmur')
        data = ["apple", "banana", "grape", "orange", "watermelon"]

        for item in data:
            bf.add(item)
            self.assertTrue(bf.contains(item))

        for _ in range(10 ** 5):
            random_string = "random" + str(_)
            bf.contains(random_string)  # Just to ensure no errors occur

if __name__ == "__main__":
    unittest.main()
