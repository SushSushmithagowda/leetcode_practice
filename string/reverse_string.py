#Implement a function to reverse a string in-place.

def reverse_string(s):
  return s[::-1]
s = "sushmitha"
print(reverse_string(s))
#time complexity: is O(n) where n is the length of the string. Slicing creates a new string in the memory that has to copy all the characters from the original string
#space complexity: is O(n) where n is the length of the string. It creates a new string and copies all the characters from the original string but in reverse order
#why is it efficient? : it leverages powerful python slicing capabilities to perform the reversal in a single line of code



#TO REVERSE A STRING IN-PLACE WITHOUT HAVING TO TAKE UP ADDITIONAL SPACE
def reverse_string_in_place(s):
    # Convert the string to a list to allow in-place modifications
    char_list = list(s)
    left, right = 0, len(char_list) - 1

    # Swap the characters from the beginning and end of the list moving towards the center
    while left < right:
        # Swap characters at left and right indices
        char_list[left], char_list[right] = char_list[right], char_list[left]
        # Move towards the center
        left += 1
        right -= 1

    # Convert the list back to a string and return
    return ''.join(char_list)

# Example usage
s = "sushmitha"
print(reverse_string_in_place(s))  # Output: "ahtimhsus"

#time complexity: is O(n) where n is the length of the string. We iterate through half of the string (n/2 swaps), which simplifies to O(n)
#space complexity: is O(n) where n is the length of the string. we create a list of characters from a string which takes additional space proportional to the length of the string
#why is it efficient?: this is efficient in terms of time and space complexity, reversing a string in place has to inspect and swap each character, leading to a linear time complexity O(n)
