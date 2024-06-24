import unittest
from BloomFilter import BloomFilter

class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.capacity = 10 ** 5
        self.error_rate = 0.01
        self.data = ["apple", "banana", "grape", "orange", "watermelon"]

    def test_add_and_contains(self):
        bf = BloomFilter(self.capacity, self.error_rate)
        for item in self.data:
            bf.add(item)
            self.assertTrue(bf.contains(item))

    def test_false_positive_rate(self):
        bf = BloomFilter(self.capacity, self.error_rate)
        for item in self.data:
            bf.add(item)

        false_positives = 0
        for _ in range(10 ** 5):
            random_string = "random" + str(_)
            if bf.contains(random_string):
                false_positives += 1

        false_positive_rate = false_positives / (10 ** 5)
        self.assertLessEqual(false_positive_rate, self.error_rate)

    def test_edge_cases(self):
        bf = BloomFilter(self.capacity, self.error_rate)
        bf.add("")
        self.assertTrue(bf.contains(""))

        special_chars = "!@#$%^&*()"
        bf.add(special_chars)
        self.assertTrue(bf.contains(special_chars))

if __name__ == "__main__":
    unittest.main()
