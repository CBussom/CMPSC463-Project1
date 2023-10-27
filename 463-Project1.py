import random
import time

MIN_MERGE = 32  # Minimum length for a run, a constant value

def calcMinRun(n):
    """
    Returns the minimum length of a run from 23 - 64 so that
    the len(array)/minrun is less than or equal to a power of 2.
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r  # Calculate the minimum run length

# This function sorts array from left index to right index
# which is of size at most RUN
def insertionSort(arr, left, right):
    # Insertion sort for small subarrays
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

# Merge function merges the sorted runs
def merge(arr, l, m, r):
    # Merge two sorted arrays
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining elements of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

# Iterative TimSort function to sort the array
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    # Start merging from size RUN (or 32) and increase in size
    size = minRun
    while size < n:

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size

# Driver program to test TimSort
if __name__ == "__main":

    arr = [-2, 7, 15, -14, 0, 15, 0,
           7, -7, -4, -13, 5, 8, -14, 12]

    print("Given Array is")
    print(arr)

    # Function Call
    timSort(arr)

    print("After Sorting Array is")
    print(arr)

# Functions to generate random and partially sorted data for testing
def generate_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

def generate_partially_sorted_data(size):
    data = list(range(1, size + 1))
    for i in range(size // 5):
        j = random.randint(0, size - 1)
        k = random.randint(0, size - 1)
        data[j], data[k] = data[k], data[j]
    return data

# Function to test TimSort on random and partially sorted data
def test_timsort():
    test_time = time.time()
    for size in [10,100,1000,10000,100000,1000000]:
        # Test on random data
        random_data = generate_random_data(size)
        sorted_data = sorted(random_data)
        timSort(random_data)
        assert random_data == sorted_data
        print(f"Random data test passed for size: {size}")
        

        # Test on partially sorted data
        partially_sorted_data = generate_partially_sorted_data(size)
        sorted_data = sorted(partially_sorted_data)
        timSort(partially_sorted_data)
        assert partially_sorted_data == sorted_data
        print(f"Partially sorted data test passed for size: {size}")

    print("total run time: ",time.time() - test_time, " seconds")

test_timsort()