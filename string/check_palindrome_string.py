#Check if a string is palindrome. Determine whether a string is a palindrome(reads the same forwards and backwards)

#using pointers to check whether a string is palindrome or not
def is_palindrome(s):
  left, right = 0, len(s) - 1

  while left < right:
    if s[left] == s[right]:
      left += 1
      right -= 1
    else:
      return False
  return True

s = "cococ"
print(is_palindrome(s))

#time complexity?: is O(n) where n is the length of the string. We potentially check each character exactly once, the comparsion is made for each pairs of characters from the end to the center.
#space complexity?: is O(1) as we only use few extra variables i.e., left and right pointer irrespective of the length of the string. No additional space proportional to the input size is used.
#how efficient? : 1. is efficient as it makes a linear scan through the string, making comparisons in constant time and using a minimal amount of extra space
# 2.using two pointers to compare characters from the end until the center ensures that we only iterate once through the string,making the check in O(n) time
#3.the in-place comparison with constant space usage makes it both time efficient and space efficient


#using slicing operation to check whether a string is palindrome or not
def palindrome_check(s):
  return s==s[::-1]
s = "sushmitha"
print(palindrome_check(s))

#time complexity: is O(n) where n is the length of the string. Since we are using slicing operation, this requires O(n) time to copy all characters from the original string
#-additionally, checking the equality of the original and the reversed string takes up O(n) time as it needs to compare each characters among the original and the reversed string
#- time complexity would be - O(n) + O(n) = O(n)

#space complexity: is O(n) where n is the length of the string. since slicing operation create a new string to store the reverse characters hence needs additional O(n) space
# - the comparison itself uses O(n) additional space

#efficiency?: The creation of a new string for the reversed version requires additional memory proportional to the length of the input string. This can be inefficient in terms of space, especially for very large strings.
#-Even though the time complexity is O(n), the method involves creating and storing a new string, which may not be optimal in memory-constrained environments.
