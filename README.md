# MSCS_532_HPC_DATA_OPTIMIZATION
# Improving Computational Efficiency Through Data Structure Optimization

## Project Summary
This project demonstrates how selecting an appropriate data structure can improve performance in computation-heavy environments such as high-performance computing (HPC).

The prototype compares two methods for duplicate detection:
1. A list-based method that performs repeated searches
2. A set-based method that uses hashing for faster lookup

## Objective
The purpose of this project is to show that performance optimization does not always require a complex algorithm. In many cases, using a more suitable data structure can significantly reduce execution time.

## Optimization Technique Used
The selected optimization technique is hash-based lookup using Python sets.

- List membership check: O(n)
- Set membership check: O(1) average case

Because of this difference, the set-based method performs better as the dataset size increases.

## Files Included
- `performance_analysis.py` - Python implementation of both approaches
- `README.md` - Project explanation and run instructions
- `requirements.txt` - Dependency file for the project

## How to Run
1. Make sure Python 3 is installed
2. Open terminal or command prompt
3. Run:

```bash
python performance_analysis.py