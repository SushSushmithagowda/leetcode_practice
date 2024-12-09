#a) Given an array of integers, find a triplet that sum up to a specific target

def threesum(arr, target):

  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      for k in range(j+1, len(arr)):
        if arr[i] + arr[j] + arr[k] == target:
          return [i, j, k]

arr = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the target value: "))
result = threesum(arr, target)
print(result)

#b) Given an array of integers, find all unique triplets that sum up to a specific target

def threesum(arr, target):
  triplets = []
  n = len(arr)

  for i in range(n-2): #The loop for i in range(n - 2): is designed to
  #ensure that there are enough elements left in the array for the other two pointers (j and k) to exist.
  #This avoids index out-of-bounds errors and reduces unnecessary iterations.
    for j in range(i+1, n-1):
      for k in range(j+1, n):
        if arr[i] + arr[j] + arr[k] == target:
          triplets.append([arr[i], arr[j], arr[k]])
  return triplets
arr = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the target value: "))
result = threesum(arr, target)
print(result)

#time complexity of O(n^3), which may not be efficient for large arrays

#c) optimized code
def threeSumTarget(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):
        # Skip the same elements to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result
nums = [1, 2, -2, -1, 0, 3]
target = 1
print(threeSumTarget(nums, target))  # Output: [[-2, 0, 3], [-1, 1, 1]]

#time complexity: Sorting the array takes O(nlogn).The main loop runs O(n) times, and for each element, the two-pointer scan runs in  O(n) time.
# - Hence, the overall time complexity is O(n2)

#space complexity: The space complexity is O(1) if we don't consider the space used to store the result.The space complexity is O(k), where k is the number of triplets in the result if we consider the output space.
