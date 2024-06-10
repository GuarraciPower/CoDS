import time
import psutil
import random
import string
from BloomFilter import BloomFilter

def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def memory_usage_psutil():
    # return the memory usage in MB
    process = psutil.Process()
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

def cpu_usage_psutil():
    # return the CPU usage as a percentage
    process = psutil.Process()
    return process.cpu_percent(interval=1.0)

def benchmark_bloom_filter(capacity, error_rate, num_elements):
    bf = BloomFilter(capacity, error_rate)
    
    start_time = time.time()
    start_mem = memory_usage_psutil()
    start_cpu = cpu_usage_psutil()

    # Adding elements to BloomFilter
    for _ in range(num_elements):
        bf.add(random_string())

    add_time = time.time() - start_time
    add_mem = memory_usage_psutil() - start_mem
    add_cpu = cpu_usage_psutil() - start_cpu

    print(f"Time to add {num_elements} elements: {add_time:.2f} seconds")
    print(f"Memory usage to add elements: {add_mem:.2f} MB")
    print(f"CPU usage to add elements: {add_cpu:.2f}%")

    start_time = time.time()
    start_mem = memory_usage_psutil()
    start_cpu = cpu_usage_psutil()

    # Checking elements in BloomFilter
    false_positives = 0
    for _ in range(num_elements):
        if bf.contains(random_string()):
            false_positives += 1

    check_time = time.time() - start_time
    check_mem = memory_usage_psutil() - start_mem
    check_cpu = cpu_usage_psutil() - start_cpu

    print(f"Time to check {num_elements} elements: {check_time:.2f} seconds")
    print(f"Memory usage to check elements: {check_mem:.2f} MB")
    print(f"CPU usage to check elements: {check_cpu:.2f}%")
    print(f"False positive rate: {false_positives / num_elements:.2%}")

if __name__ == "__main__":
    capacity = 10000
    error_rate = 0.01
    num_elements = 1000
    
    print(f"Benchmarking Bloom Filter with capacity {capacity}, error rate {error_rate}, and {num_elements} elements.")
    benchmark_bloom_filter(capacity, error_rate, num_elements)
