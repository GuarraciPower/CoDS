import json
import time
import psutil
import random
import string
import os
from BloomFilter import BloomFilter

def load_data(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()

def memory_usage_psutil():
    process = psutil.Process()
    mem = process.memory_info().rss / float(2 ** 20)
    return mem

def cpu_usage_psutil():
    process = psutil.Process()
    return process.cpu_percent(interval=1.0)

def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def benchmark_bloom_filter(data, capacity, error_rate, hash_function='jenkins'):
    bf = BloomFilter(capacity, error_rate, hash_function)

    add_times = []
    check_times = []
    false_positives = 0

    for i, item in enumerate(data):
        start_time = time.time()
        bf.add(item)
        add_time = time.time() - start_time
        add_times.append(add_time)

        start_time = time.time()
        if bf.contains(random_string()):
            false_positives += 1
        check_time = time.time() - start_time
        check_times.append(check_time)

    false_positive_rate = false_positives / len(data)
    actual_bit_usage = sum(bin(x).count('1') for x in bf.bitset.bitset)
    compression_rate = actual_bit_usage / bf.bitset.size

    return {
        "add_time": add_times,
        "check_time": check_times,
        "false_positive_rate": [false_positive_rate] * len(data),
        "compression_rate": compression_rate,
        "memory_usage": memory_usage_psutil()
    }


def benchmark_linear_search(data):
    add_times = []
    search_times = []

    elements_list = []

    for i in range(1, len(data) + 1):
        start_time = time.time()
        elements_list.append(data[i - 1])
        add_time = time.time() - start_time
        add_times.append(add_time)

        start_time = time.time()
        elements_list.index(data[i - 1])
        search_time = time.time() - start_time
        search_times.append(search_time)

    return {
        "add_time": add_times,
        "search_time": search_times,
        "memory_usage": memory_usage_psutil()
    }


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_bst_iterative(root, value):
    if root is None:
        return BSTNode(value)

    current = root
    while True:
        if value < current.value:
            if current.left is None:
                current.left = BSTNode(value)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = BSTNode(value)
                break
            current = current.right
    return root


def search_bst(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search_bst(root.left, value)
    return search_bst(root.right, value)


def benchmark_bst(data):
    random.shuffle(data)  # Randomize the data before insertion

    add_times = []
    search_times = []

    root = None

    for i in range(1, len(data) + 1):
        start_time = time.time()
        root = insert_bst_iterative(root, data[i - 1])
        add_time = time.time() - start_time
        add_times.append(add_time)

        start_time = time.time()
        search_bst(root, data[i - 1])
        search_time = time.time() - start_time
        search_times.append(search_time)

    return {
        "add_time": add_times,
        "search_time": search_times,
        "memory_usage": memory_usage_psutil()
    }


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def insert_avl(root, key):
    if not root:
        return AVLNode(key)
    elif key < root.key:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def left_rotate(z):
    if z.right is None:
        return z
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y


def right_rotate(z):
    if z.left is None:
        return z
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y


def get_height(root):
    if not root:
        return 0
    return root.height


def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)


def search_avl(root, key):
    if not root or root.key == key:
        return root
    if key < root.key:
        return search_avl(root.left, key)
    return search_avl(root.right, key)


def benchmark_avl_tree(data):
    random.shuffle(data)  # Randomize the data before insertion

    add_times = []
    search_times = []

    root = None

    for i in range(1, len(data) + 1):
        start_time = time.time()
        root = insert_avl(root, data[i - 1])
        add_time = time.time() - start_time
        add_times.append(add_time)

        start_time = time.time()
        search_avl(root, data[i - 1])
        search_time = time.time() - start_time
        search_times.append(search_time)

    return {
        "add_time": add_times,
        "search_time": search_times,
        "memory_usage": memory_usage_psutil()
    }


if __name__ == "__main__":
    capacity = 10 ** 6
    error_rate = 0.01
    num_elements = 10 ** 6

    data_files = {
        "Natural Language Words": "data/natural_language_words.txt",
        "Random Strings": "data/random_strings.txt",
        "DNA Sequences": "data/dna_sequences.txt",
        "Email Addresses": "data/email_addresses.txt"
    }

    results = {}

    for data_type, file_path in data_files.items():
        data = load_data(file_path)
        results[data_type] = {
            "bloom_filter": {},
            "linear_search": benchmark_linear_search(data),
            "bst": benchmark_bst(data),
            "avl_tree": benchmark_avl_tree(data)
        }
        print(
            f"Benchmarking Bloom Filter with {data_type} (capacity {capacity}, error rate {error_rate}, {num_elements} elements)."
        )
        for hash_function in ['jenkins', 'murmur', 'city', 'sha256']:
            results[data_type]["bloom_filter"][hash_function] = benchmark_bloom_filter(
                data, capacity, error_rate, hash_function)

    os.makedirs("results", exist_ok=True)
    with open("results/benchmark_results.json", "w") as file:
        json.dump(results, file, indent=4)

    print("Benchmarking completed and results saved to results/benchmark_results.json")
