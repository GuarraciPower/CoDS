import hashlib
import mmh3
import cityhash


class HashFunctions:
    @staticmethod
    def hash_int32_jenkins(key):
        if isinstance(key, str):
            key = key.encode('utf-8')
        print("JenkinsHash input:", key)
        hash_value = 0
        for char in key:
            hash_value += char
            hash_value += (hash_value << 10)
            hash_value ^= (hash_value >> 6)
        hash_value += (hash_value << 3)
        hash_value ^= (hash_value >> 11)
        hash_value += (hash_value << 15)
        return hash_value & 0xffffffff

    @staticmethod
    def hash_int32_shift(key):
        if isinstance(key, str):
            key = key.encode('utf-8')
        print("ShiftHash input:", key)
        hash_value = 0
        for char in key:
            hash_value = (hash_value << 5) - hash_value + char
        return hash_value & 0xffffffff

    @staticmethod
    def hash_murmur(key):
        if isinstance(key, str):
            key = key.encode('utf-8')
        print("MurmurHash input:", key)
        return mmh3.hash(key)

    @staticmethod
    def hash_city(key):
        if isinstance(key, str):
            key = key.encode('utf-8')
        print("CityHash input:", key)
        return cityhash.CityHash32(key)

    @staticmethod
    def hash_sha256(key):
        if isinstance(key, str):
            key = key.encode('utf-8')
        print("SHA-256 input:", key)
        return int(hashlib.sha256(key).hexdigest(), 16) % (1 << 32)

    @staticmethod
    def hash_string(item):
        if isinstance(item, str):
            item = item.encode('utf-8')
        print("Hash String input:", item)
        return int(hashlib.md5(item).hexdigest(), 16)
