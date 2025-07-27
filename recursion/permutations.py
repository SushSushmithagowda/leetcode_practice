#Permutations: Generate all permutations of a given string using recursion.

# solving using recursion approach
#what is permutation?
# permutation and combination are both fundamental concepts in combinatorics, dealing with the arrangement of objects
#permuattion: It refer to the arrangement of objects in a specific order. The formula for permutation for arranging r objects from n objects is
# p = n!/(n - r)!

def permutations(s):
  if len(s) <= 1: #base case
    return [s]
  perms = []
  for i, c in enumerate(s):
    for perm in permutations(s[:i] + s[i+1:]):
      perms.append(c + perm)
  return perms
s = "abc"
print(permutations(s))

#time complexity: would be O(n!) because for each character in a given string, the function generates (n-1) recursive calls and then (n-2) for those recursive calls
# and so on resulting in n! permutations

#space complexity: would be O(n!) because there are n! permutations of the input string s and each permutation requires a new string which results in exponential
# - space usage
