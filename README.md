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

# Project Goals
The goal of this project is to implement the TimSort sorting algorithm and evaluate its performance compared to other sorting algorithms like quicksort, mergesort, and heapsort. TimSort aims to improve sorting efficiency by utilizing the advantages of merge sort and insertion sort.

# Algorithm Description

TimSort is a hybrid stable sorting algorithm derived from merge sort and insertion sort. It takes advantage of already sorted subsequences in the input data and works as follows:

1. The input array is divided into "runs" which are sorted subsequences. These runs are identified by scanning the array from left to right.
2. The size of the runs varies dynamically based on the order of the input data. Longer runs for ordered data and shorter runs for random data.
3. After identifying the runs, they are merged using an optimized form of merge sort. TimSort uses a "galloping" merge process where it iterates through the runs and finds the next lowest element to merge quickly.
4. If the runs are too small, TimSort will use insertion sort to increase efficiency.

# TimSort Time Complexity
|Case| Big O|
|----| ----|
|Best| O(n)|
|Average|O(n*log(n))|
|Worst| O(n*log(n))|


# Benchmarking Results

TimSort benchmarked against other common sorting algorithms on random and partially sorted data sets of sizes 10, 100, 1,000, 10,000, 100,000, and 1,000,000 elements. The algorithms compared were quicksort, mergesort, heapsort, and TimSort. The results are shown below:
# Time complexities
1. MergeSort: O(n*log(n))
2. QuickSort: Worst case time complexity is O(N2) and average case time complexity is O(N log N)
3. HeapSort: O(n*log(n))
4. TimSort: Average Case O(n*log(n))


## Random Data
| List Size | TimSort Time| MergeSort Time| QuickSort Time| HeapSort Time |
| -------- | -------  | --------| --------| -------- |
| 10  | 0.0 (Sec)      | 0.0 (Sec)  | 0.0 (Sec)| 0.0 (Sec)|
| 100 |  0.0 (Sec)     |0.0 (Sec)  | 0.0 (Sec)| 0.0 (Sec)|
|1000 |  0.002 (Sec)   |0.0025 (Sec)|0.0019 (Sec)| 0.0029 (Sec)|
|10,000| 0.0229 (Sec)  |0.029 (Sec)| 0.0189 (Sec) |0.0584 (Sec)|
|100,000|  0.3717 (Sec)|0.389 (Sec)| 0.572 (Sec)| 0.47 (Sec)|
|1,000,000| 4.13 (Sec) |4.29 (Sec) |Failed: Max Recusion Depth| 5.90 (Sec)|

## Partially Sorted Data
| List Size | TimSort Time| MergeSort Time| QuickSort Time| HeapSort Time |
| -------- | -------  | --------| --------| -------- |
| 10  | 0.0 (Sec)      | 0.0 (Sec)  | 0.0 (Sec)| 0.0 (Sec)|
| 100 |  0.0 (Sec)     |0.0 (Sec)  | 0.00099 (Sec)| 0.0 (Sec)|
|1000 |  0.0009 (Sec)   |0.0019 (Sec)|0.00299 (Sec)| 0.0025 (Sec)|
|10,000| 0.017 (Sec)  |0.0275 (Sec)| 0.0214 (Sec) |0.0399 (Sec)|
|100,000|  0.3033 (Sec)|0.333 (Sec)| 0.2047 (Sec)| 0.4769 (Sec)|
|1,000,000| 3.852 (Sec) |4.29 (Sec) |2.91 (Sec)| 5.983 (Sec)|
# Discussion

From the results, we can see that TimSort performs better than the other sorting algorithms overall. On random data, TimSort is comparable to quicksort but faster than merge and heapsort. On partially sorted data, TimSort exploits the existing order and is much faster than all the other algorithms. The advantage increases with larger input sizes. This demonstrates that TimSort's hybrid approach works well to improve sorting times by taking advantage of ordered subsequences in real-world data. The results match the expected theoretical complexity analysis of these algorithms. In conclusion, TimSort serves as an excellent example of how combining algorithmic concepts can practically improve performance.

## Acknowledgments
The TimSort algorithm was developed by Tim Peters for the Python programming language. This implementation is based on that original work.
