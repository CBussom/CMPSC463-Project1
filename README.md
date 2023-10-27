# TimSort - A Python Sorting Algorithm

## Introduction
TimSort is a hybrid sorting algorithm derived from merge sort and insertion sort. It is designed to perform well on many kinds of real-world data and is particularly effective on input data that is already partially ordered. The algorithm first divides the list into small chunks and sorts each chunk using insertion sort, and then merges these sorted chunks using merge sort.

This repository contains an implementation of the TimSort algorithm in Python, along with test cases to verify its correctness and performance.

## TimSort Algorithm
The main components of the TimSort algorithm in this implementation are as follows:

- `calcMinRun(n)`: Calculates the minimum run length for a given input size, ensuring that the ratio `len(array) / minrun` is less than or equal to a power of 2. This helps in determining the run length for sorting.

- `insertionSort(arr, left, right)`: Sorts a small subarray using insertion sort. It is used for sorting subarrays of size at most the minimum run length.

- `merge(arr, l, m, r)`: Merges two sorted subarrays into a single sorted array. This is a key step in the merge sort part of TimSort.

- `timSort(arr)`: The main TimSort function. It first divides the input array into runs and sorts each run using insertion sort. Then, it repeatedly merges runs to create larger sorted runs until the entire array is sorted.

## Testing TimSort
The `test_timsort` function in this repository is used to test the TimSort implementation. It covers random and partially sorted data sets of various sizes (10, 100, 1000, 10000, 100000, and 1000000 elements). The test cases ensure that the algorithm correctly sorts data, and it also measures the total execution time for performance evaluation.


## Performance
TimSort is known for its efficiency on various data types and distributions. The test cases provided here demonstrate its effectiveness in sorting both random and partially sorted data sets.

## Acknowledgments
The TimSort algorithm was developed by Tim Peters for the Python programming language. This implementation is based on that original work.
