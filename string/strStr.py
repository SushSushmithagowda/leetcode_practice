#Implement strStr(): Implement the strStr() function to find the index of the first occurence of a substring in a string It takes two arguments: the main string (the string to search within) and the substring (the string to search for).
#It iterates through the main string and checks if any substring matches the substring being searched for.

#If a match is found, it returns the index of the start of the substring within the main string. If no match is found, it returns -1.


def substring_match(main_str, sub_str):
  for i in range(len(main_str) - len(sub_str) + 1): #ensures that the substring comparison does not go out of bounds.
    if main_str[i:i+len(sub_str)] == sub_str: # its 0:0+2 = su
      return i
  return -1

main_str = "sushmitha"
sub_str = "mi"
print(substring_match(main_str, sub_str))

#time complexity: is O(n.m) where n is teh sub string and m is the main string in the outer loop. Each iteration it compares the sub string from the main string so, its O(n)
# - overall time complexity is O(n.m)
#space complexity: the code uses a fixed amount of space for the i loop variable and the input string. the slice when comparing creates a new substring in each iteartion
# - but this temporary space is constant with respect to the input size and does not grow with the grow in the input size so it is O(1)

