import json
import time
import psutil
import random
import string
import os
import matplotlib.pyplot as plt
from BloomFilter import BloomFilter

def load_data(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()

def memory_usage_psutil():
    process = psutil.Process()
    mem = process.memory_info().rss / float(2 ** 20)
    return mem

def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def analyze_false_positive_rate(data, capacity, error_rate, hash_function='jenkins'):
    bf = BloomFilter(capacity, error_rate, hash_function)

    false_positive_rates = []
    false_positives = 0

    for i, item in enumerate(data):
        bf.add(item)
        if bf.contains(random_string()):
            false_positives += 1

        false_positive_rate = false_positives / (i + 1)
        false_positive_rates.append(false_positive_rate)

    return false_positive_rates

def analyze_compression_rate(data, capacities, error_rates, hash_function='jenkins'):
    results = []

    for capacity in capacities:
        for error_rate in error_rates:
            bf = BloomFilter(capacity, error_rate, hash_function)
            for item in data:
                bf.add(item)

            actual_bit_usage = sum(bin(x).count('1') for x in bf.bitset.bitset)
            compression_rate = actual_bit_usage / bf.bitset.size

            false_positives = 0
            for _ in range(10000):  # Test with 10,000 random strings
                if bf.contains(random_string()):
                    false_positives += 1

            observed_false_positive_rate = false_positives / 10000

            results.append({
                'capacity': capacity,
                'error_rate': error_rate,
                'compression_rate': compression_rate,
                'observed_false_positive_rate': observed_false_positive_rate
            })

    return results

def plot_false_positive_rate(results, title):
    plt.figure(figsize=(12, 8))
    for label, rates in results.items():
        plt.plot(rates, label=label)
    plt.title(title)
    plt.xlabel("Number of Elements Added")
    plt.ylabel("False Positive Rate")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"results/{title.replace(' ', '_').lower()}.png")
    plt.close()

def plot_compression_rate(results, title, x_key, y_key):
    plt.figure(figsize=(12, 8))
    for result in results:
        plt.scatter(result[x_key], result[y_key], label=f"Capacity: {result['capacity']}, Error Rate: {result['error_rate']}")
    plt.title(title)
    plt.xlabel(x_key.replace('_', ' ').title())
    plt.ylabel(y_key.replace('_', ' ').title())
    plt.legend()
    plt.grid(True)
    plt.savefig(f"results/{title.replace(' ', '_').lower()}.png")
    plt.close()

def main():
    capacity = 10000
    error_rate = 0.01
    num_elements = 15000  # Exceed the designed capacity to test false positive rate changes

    data_files = {
        "Natural Language Words": "data/natural_language_words.txt",
        "Random Strings": "data/random_strings.txt",
        "DNA Sequences": "data/dna_sequences.txt",
        "Email Addresses": "data/email_addresses.txt"
    }

    results_q7 = {}
    results_q8 = []

    os.makedirs("results", exist_ok=True)

    for data_type, file_path in data_files.items():
        data = load_data(file_path)[:num_elements]  # Limit data to num_elements

        # Question 7: False Positive Rate Analysis
        results_q7[data_type] = analyze_false_positive_rate(data, capacity, error_rate, hash_function='jenkins')

        # Question 8: Compression Rate Analysis
        capacities = [5000, 10000, 20000]
        error_rates = [0.001, 0.01]
        results_q8.extend(analyze_compression_rate(data, capacities, error_rates, hash_function='jenkins'))

    # Plot results for Question 7
    plot_false_positive_rate(results_q7, "False Positive Rate Over Time")

    # Plot results for Question 8
    plot_compression_rate(results_q8, "Compression Rate vs Expected False Positives", 'error_rate', 'compression_rate')
    plot_compression_rate(results_q8, "Compression Rate vs Observed False Positives", 'observed_false_positive_rate', 'compression_rate')

    # Save results to JSON for further inspection
    with open("results/q7_results.json", "w") as file:
        json.dump(results_q7, file, indent=4)

    with open("results/q8_results.json", "w") as file:
        json.dump(results_q8, file, indent=4)

if __name__ == "__main__":
    main()
