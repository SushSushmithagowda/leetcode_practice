def maxtwosum(arr):
  largest = second_largest = float('-inf')

  for num in arr:
    if num > largest:
      second_largest = largest
      largest = num
    elif num > second_largest:
      second_largest = num

  max_sum = largest + second_largest
  return max_sum

arr = list(map(int, input("Enter the elements in an array: ").split()))
result = maxtwosum(arr)
print(result)
