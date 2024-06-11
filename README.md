# Concepts of Data Science
## Project overview

The purpose of the project is the implementation of a Bloom filter. The concept of
this data structure was explained and additional information on this data structure 
can be found online, for instance on [Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter).
1. The development of the software should be done using version control
    hosted on GitHub or Gitlab. The repository should also contain a
    README file that documents the content of the repository, as well as a
    summary of your conclusions.
2. The Bloom filter should be either implemented using an object-oriented
    approach, or a functional approach. Clearly, code quality is important. The
    code should be easy to read and documented clearly. The data structure is 
    implemented in Python as a module, so that it can be used in a Jupyter notebook 
    for demonstration purposes and testing, but also from a Python script for
    benchmarking on the HPC infrastructure.
3. The implementation must be tested thoroughly for correctness.
4. To implement a Bloom filter, it's necessary to define a family of hash 
    functions. These hash functions should be tested to verify that they produce
    appropriate values. Note that these hash functions may work well for
    certain data (e.g., natural language words) but not so well for other data
    (e.g., random strings or DNA). Test with at least two data types.
5. Discuss the expected time and space complexity of the implementation.
6. The performance of the implementation has to be tested as well using a
    large data sample. The insert and search functions should be timed for an 
    increasing number of words and plots need to be created. These benchmarks 
    should be performed on the HPC infrastructure. Include the job script and 
    the Python test script in the repository, as well as the output of the 
    benchmark runs. Consult the [VSC documentation](https://docs.vscentrum.be/) 
    if necessary.
7. Checks on how the false positive rate changes as a function of the number 
    of words inserted in the Bloom filter should be implemented. Also if the number 
    of words exceeds the expected number of words for which the Bloom filter was
    designed.
8. Checks on the compression rate of the Bloom filter as a function of the expected
    number of and the rate of false positives should also be implemented.

# Bloom Filter Implementation

## Description

This project implements a Bloom Filter in Python. A Bloom Filter is a probabilistic 
data structure that allows for efficient set membership checks with a configurable 
false positive rate.

## Files

- `BitSet.py`: Implements the BitSet class to handle the bit array.
- `HashFunctions.py`: Provides various hash functions used by the Bloom Filter.
- `BloomFilter.py`: The main Bloom Filter implementation.
- `benchmark.py`: Script to benchmark the Bloom Filter implementation.

## Usage

To use the Bloom Filter, import the `BloomFilter` class from `BloomFilter.py` and 
create an instance with desired capacity and error rate.

## Testing

Tests are provided to verify the correctness of the Bloom Filter and hash functions.

## Benchmarking

The `benchmark.py` script benchmarks the performance of the Bloom Filter by measuring 
time, memory, and CPU usage.

## Time and Space Complexity

- **Time Complexity**: O(k) for insert and lookup operations, where k is the number of 
                        hash functions.
- **Space Complexity**: O(m) for the bit array, where m is the size of the bit array.

## Performance Testing

Performance tests include adding and checking elements in the Bloom Filter and measuring 
the false positive rate and compression rate.

## Conclusion

TBD

## Future Work

- Further optimization of hash functions.
- Extended performance tests on different datasets.
- Integration with Jupyter notebooks for demonstration purposes.
