#Question: Given an array nums, return an array output where output[i] is equal to the product of all the elements of nums except nums[i]
#without using division operator - this is the question asked in leetcode
def product_except_self(nums):

  res = [1] * len(nums)
  prefix = 1

  for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]

  postfix = 1

  for i in range(len(nums) -1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]
  return res

nums = [1, 2, 3, 4]
print(product_except_self(nums))

#time complexity: The first for loop runs from 0 to len(nums) - 1 (inclusive), performing O(n) operations. The second for loop runs from len(nums) - 1 to 0 (inclusive), performing O(n) operations.
# - Since both loops run sequentially and not nested, the overall time complexity is O(n) + O(n) = O(n)

#space complexity: The space complexity consists of the space used by the res list and the variables prefix and postfix. The res list has a size of n (same as the input list nums),
# - which is O(n). The prefix and postfix variables use O(1) space each. The overall space complexity is O(n) for the res list. The additional space used by prefix and postfix is constant, so it does not affect the asymptotic space complexity.

#using division operator
def product_except_self(nums):
  product = 1
  zero_count = 0

  n = len(nums)
  for num in nums:
    if num != 0:
      product *= num
    else:
      zero_count += 1

  #if there is one zero
  if zero_count == 1:
    return [product if num == 0 else 0 for num in nums]

  #if there are more than one zeros
  if zero_count > 1:
    return [0] * n

  #if there are no zeros
  return [product // num for num in nums]


nums = [1, 2, 3, 4]
print(product_except_self(nums))
