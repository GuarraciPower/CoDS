import os
import random
import string

# Define the number of elements in the datasets
NUM_ELEMENTS = 10 ** 6


# Generate random strings related to computer science
def generate_random_strings(file_path, num_strings, length=10):
    keywords = ["algorithm", "binary", "compiler", "data", "encryption", "function", "hardware", "interface", "java", "kernel", "library", "memory", "network", "object", "protocol", "queue", "recursion", "syntax", "thread", "variable"]
    with open(file_path, 'w') as f:
        for _ in range(num_strings):
            rand_str = ''.join(random.choices(keywords, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=length - 1))
            f.write(rand_str + '\n')


# Generate natural language words related to data science
def generate_natural_language_words(file_path, num_words):
    words = ["data", "science", "machine", "learning", "model", "algorithm", "statistics", "analysis", "big", "data", "mining", "predictive", "analytics", "visualization", "clustering", "classification", "regression", "python", "r", "sql"]
    with open(file_path, 'w') as f:
        for _ in range(num_words):
            f.write(random.choice(words) + '\n')


# Generate real-world DNA sequences
def generate_dna_sequences(file_path, num_sequences, length=10):
    nucleotides = ['A', 'T', 'C', 'G']
    with open(file_path, 'w') as f:
        for _ in range(num_sequences):
            seq = ''.join(random.choices(nucleotides, k=length))
            f.write(seq + '\n')


# Generate email addresses with specific domains
def generate_email_addresses(file_path, num_addresses):
    domains = ["hotmail.com", "outlook.com", "gmail.com", "uhasselt.be", "kuleuven.be"]
    with open(file_path, 'w') as f:
        for _ in range(num_addresses):
            user = ''.join(random.choices(string.ascii_lowercase, k=5))
            domain = random.choice(domains)
            f.write(user + "@" + domain + '\n')


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    generate_random_strings("data/random_strings.txt", NUM_ELEMENTS)
    generate_natural_language_words("data/natural_language_words.txt", NUM_ELEMENTS)
    generate_dna_sequences("data/dna_sequences.txt", NUM_ELEMENTS)
    generate_email_addresses("data/email_addresses.txt", NUM_ELEMENTS)
