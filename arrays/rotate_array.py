#Rotate an array 'nums' 'k' steps to the right, Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#approach - in-place with O(1) extra space
#refer the solved leetcode problem
def rotate_array(nums, k):
  #if k is greater than the length of the array, it wraps around appropriately
  k = k % len(nums)

  l, r = 0, len(nums) - 1
  while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1

  l, r = 0, k - 1
  while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1

  l, r = k, len(nums) - 1
  while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array(nums, k))
# time complexity: is O(n) because reversing the array three times each takes O(n) + O(n) + O(n) = O(n)
#space complexity: the algorithm performs rotation in-place without using additional memory space

#another approach but the space complexity is not constant
def rotate_array(nums, k):

  k = k % len(nums)

  return nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array(nums, k))

#time complexity: is O(n) because slicing operations takes linear time
#space complexity: O(n) because we create a new list to store the rotated array elements
