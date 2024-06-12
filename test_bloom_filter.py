import unittest
from BloomFilter import BloomFilter
from HashFunctions import HashFunctions


class TestBloomFilter(unittest.TestCase):

    def test_add_and_contains(self):
        bf = BloomFilter(100, 0.01)
        bf.add("hello")
        self.assertTrue(bf.contains("hello"))
        self.assertFalse(bf.contains("world"))

    def test_false_positives(self):
        bf = BloomFilter(1000, 0.01)
        for i in range(500):
            bf.add(f"item{i}")
        false_positives = sum(1 for i in range(500, 1000)
                              if bf.contains(f"item{i}"))
        self.assertLess(false_positives, 50)  # Expecting < 5% false positives

    def test_hash_functions(self):
        data = ["hello", "world", "foo", "bar"]
        hashes = [HashFunctions.hash_int32_jenkins(d) for d in data]
        self.assertEqual(len(hashes), len(set(hashes)))  # Ensure no collisions


if __name__ == '__main__':
    unittest.main()
