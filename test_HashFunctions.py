import unittest
from HashFunctions import HashFunctions

class TestHashFunctions(unittest.TestCase):
    def test_hash_int32_jenkins(self):
        result = HashFunctions.hash_int32_jenkins("test")
        self.assertIsNotNone(result)

    def test_hash_int32_shift(self):
        result = HashFunctions.hash_int32_shift("test")
        self.assertIsNotNone(result)

    def test_hash_murmur(self):
        result = HashFunctions.hash_murmur("test")
        self.assertIsNotNone(result)

    def test_hash_city(self):
        result = HashFunctions.hash_city("test")
        self.assertIsNotNone(result)

    def test_hash_sha256(self):
        result = HashFunctions.hash_sha256("test")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()


