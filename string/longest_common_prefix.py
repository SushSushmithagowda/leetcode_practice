#Longest Common prefix: Find the longest common prefix string amongst an array of strings. Example: The prefix "fl" is common to all three strings. "ower", "ow", and "ight" are not common to all strings. So, the longest common prefix among ["flower", "flow", "flight"] is "fl".

def longestcommonprefix(str):
  if not str:
    return " "
  for i, char in enumerate(str[0]):
    for string in str[1:]:
      if i >= len(string) or string[i] != char:
        return str[0][:i]
  return str[0] #if neither of the above conditions are met , then this is the shortest string

str = ["flower", "flow", "flowing", "floster"]
print(longestcommonprefix(str))

#time complexity: The time complexity of the longestcommonprefix function is O(n⋅m), where n is the number of strings in the list str and m is the length of the shortest string in the list. Here's the breakdown:The outer loop iterates over the characters of the first string in str, which has a length of m.
# - The inner loop iterates over all other strings in str[1:], which are n−1 strings. In the worst case, the inner loop may compare each character of the first string with each character of all other strings, resulting in O(m⋅(n−1)) comparisons.
# - The space complexity of the function is O(1) because the space used is constant and does not scale with the input size. This is because the function does not use any additional data structures that grow with the input size; it only uses a few variables for indexing and comparison.

