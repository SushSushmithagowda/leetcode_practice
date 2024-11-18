#Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is 
# - greater than or equal to target. If there is no such subarray, return 0 instead.

def min_subarray(arr, target):

  l, total = 0, 0
  res = float("inf")

  for r in range(len(arr)):
    total += arr[r]

    while total >= target:
      res = min(r - l + 1, res)
      total -= arr[l]
      l += 1
  return 0 if res == float("inf") else res

arr = [2,3,1,2,4,3]
target = 7
print(min_subarray(arr, target))

#time complexity: is O(n) where n is the length of the input array, because the function iterates through the array once using the right pointer and increements
# - left pointer when needed resulting in linear time complexity

#space complexity: is O(1) where the algorithms uses a constant amount of extra space regardless of the input size of the array, making it space efficient
