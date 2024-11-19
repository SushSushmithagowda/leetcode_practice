#Find the contiguous subarray (containing at least one number) that has the smallest sum.

def minSum(arr):

  minSub = float("inf")
  curSum = arr[0]

  for i in range(len(arr)):
    if curSum > 0:
      curSum = 0

    curSum += arr[i]
    minSub = min(minSub, curSum)
  return minSub

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(minSum(arr))
