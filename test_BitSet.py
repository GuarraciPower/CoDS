import unittest
from BitSet import BitSet

class TestBitSet(unittest.TestCase):
    def test_add_and_contains(self):
        size = 100
        bitset = BitSet(size)
        bitset.add(10)
        self.assertTrue(bitset.contains(10))
        self.assertFalse(bitset.contains(20))

    def test_edge_cases(self):
        size = 100
        bitset = BitSet(size)
        bitset.add(0)
        self.assertTrue(bitset.contains(0))
        bitset.add(size - 1)
        self.assertTrue(bitset.contains(size - 1))

if __name__ == "__main__":
    unittest.main()
