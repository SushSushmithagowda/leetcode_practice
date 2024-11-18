#Find the contiguous subarray (containing at least one number) that has the largest sum.

#this problem is also known as Kadanes Algorithm problem
#this is kind oof sliding window approach
def max_subarray(arr):
  n = len(arr)

  maxSub = arr[0]
  curSum = 0

  for i in range(n):
    if curSum < 0:
      curSum = 0
    curSum += arr[i]
    maxSub = max(maxSub, curSum)
  return maxSub

arr = [5, 4, -1, 7, 8]
print(max_subarray(arr))

#time complexity: is O(n) where n is the size of the input array as we only iterate through the array once. Regardless of the size of the input array, the number
# of operations performed is proportional to n making it a linear time complexity

#space complexity: is O(1) as the algorithm uses constant amount of space except it needs additional space only for certain variables like maxSub, curSum,
# i which doesnt scale with the input size. therefore the space complexity is O(1)
