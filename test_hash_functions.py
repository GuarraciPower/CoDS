import os
#import random
#import string
import json
import time
import matplotlib.pyplot as plt
from HashFunctions import HashFunctions

# Define the number of elements in the datasets
NUM_ELEMENTS = 10 ** 5

def load_data(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def test_hash_function(hash_function, data):
    start_time = time.time()
    hash_values = [hash_function(item) for item in data]
    end_time = time.time()
    
    execution_time = end_time - start_time
    collision_count = len(hash_values) - len(set(hash_values))
    
    return hash_values, execution_time, collision_count

def plot_hash_distribution(hash_values, title):
    plt.figure(figsize=(12, 8))
    plt.hist(hash_values, bins=50, edgecolor='k', alpha=0.7)
    plt.title(title)
    plt.xlabel('Hash Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(f"results/{title.replace(' ', '_').lower()}.png")
    plt.close()

def main():
    data_files = {
        "Natural Language Words": "data/natural_language_words.txt",
        "Random Strings": "data/random_strings.txt",
        "DNA Sequences": "data/dna_sequences.txt"
    }
    
    hash_functions = {
        "Jenkins": HashFunctions.hash_int32_jenkins,
        "Shift": HashFunctions.hash_int32_shift,
        "Murmur": HashFunctions.hash_murmur,
        "City": HashFunctions.hash_city,
        "SHA256": HashFunctions.hash_sha256
    }

    os.makedirs("results", exist_ok=True)
    
    results = {}
    
    for data_type, file_path in data_files.items():
        data = load_data(file_path)
        results[data_type] = {}
        
        for hash_name, hash_function in hash_functions.items():
            hash_values, exec_time, collisions = test_hash_function(hash_function, data)
            results[data_type][hash_name] = {
                "execution_time": exec_time,
                "collisions": collisions
            }
            
            plot_hash_distribution(hash_values, f"{data_type} - {hash_name} Hash Distribution")
    
    with open("results/hash_function_results.json", "w") as file:
        json.dump(results, file, indent=4)
    
    print("Hash function testing completed and results saved to results/hash_function_results.json")

if __name__ == "__main__":
    main()
