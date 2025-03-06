#Binary Search: Implement binary search using iteration:

import numpy as np
def binary_search(arr, target):
  low, high = 0, len(arr) - 1
  sorted_arr = np.sort(arr)

  while low <= high:
    #why do we use (high - low)// 2 instead low + high // 2? cz if low and high are large integers, their sum high + low could exceed the maximum
    #value that the integer type can represent, leading to an overflow and potentially incorrect results. so here we ensure that the calculation is
    # is done with the difference first and then dividing by 2 to get the middle index
    mid = low + (high - low) // 2
    if sorted_arr[mid] == target:
      return mid
    elif sorted_arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

arr = [1, 2, 5, 3, 4, 6]
target = 6
print(binary_search(arr, target))

#time complexity: is O(log n) where n is the number of elements in the input array, this is 'cause with each iteration, the search space is divided in half
#space complexity: is O(1) because it requires constant amount of space regardless of the input size, because it only uses a few variable sto keep track of the indices
#efficiency? its definitely efficient and its much faster compared to linear search, especially for large arrays, as it reduces the search space exponentially
# - iteration, however it requires the array to be sorted, which might be an additional operation if the array is not already sorted
