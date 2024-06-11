# Project Concepts of Data Science
**Description:**

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
