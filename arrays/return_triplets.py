#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.

def threesum(nums):

  res = []
  nums.sort()
  n = len(nums)

  for i in range(n):
    left, right = i + 1, n - 1
    if i > 0 and nums[i] == nums[i - 1]:
      continue

    while left < right:
      total = nums[i] + nums[left] + nums[right]
      if total < 0:
        left += 1
      elif total > 0:
        right -= 1
      else:
        res.append([nums[i], nums[left], nums[right]])

        while left < right and nums[left] == nums[left + 1]:
            left += 1

        while left < right and nums[right] == nums[right - 1]:
            right -= 1

        left += 1
        right -= 1
  return res

nums = [-1, 0, 1, 2, -1, -4]
print(threesum(nums))

#time complexity: firstly we are sorting which would be O(n log n), the main loop runs in O(n) time and for each element the two pointer scan runs in O(n) time
# - hence the overall time complexity is O(n2)

#space complexity: would be O(1) if we dont consider the space to store the result
# - would be O(k) if we consider saving our result in result variable
