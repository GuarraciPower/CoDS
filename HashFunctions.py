class HashFunctions:
    @staticmethod
    def hash_int32_shift(input):
        x = input
        x = ~x + (x << 15)
        x = x ^ (x >> 12)
        x = x + (x << 2)
        x = x ^ (x >> 4)
        x = x * 2057
        x = x ^ (x >> 16)
        return x & 0xFFFFFFFF

    @staticmethod
    def hash_int32_jenkins(input):
        a = input
        a = (a + 0x7ed55d16) + (a << 12)
        a = (a ^ 0xc761c23c) ^ (a >> 19)
        a = (a + 0x165667b1) + (a << 5)
        a = (a + 0xd3a2646c) ^ (a << 9)
        a = (a + 0xfd7046c5) + (a << 3)
        a = (a ^ 0xb55a4f09) ^ (a >> 16)
        return a & 0xFFFFFFFF

    @staticmethod
    def hash_string(input):
        hash = 0
        for i in range(len(input)):
            hash += ord(input[i])
            hash += (hash << 10)
            hash ^= (hash >> 6)
        hash += (hash << 3)
        hash ^= (hash >> 11)
        hash += (hash << 15)
        return hash & 0xFFFFFFFF
