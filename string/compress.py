#Given an array of characters chars, compress it using the following algorithm:
#Begin with an empty string s. For each group of consecutive repeating characters in chars:

#If the group's length is 1, append the character to s. Otherwise, append the character followed by the group's length. The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

#After you are done modifying the input array, return the new length of the array.

#You must write an algorithm that uses only constant extra space.

#Example 1:

#Input: chars = ["a","a","b","b","c","c","c"] Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"] Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

def compress(chars):
    if not chars:
        return 0

    count = 1
    res = []

    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            count += 1
        else:
            res.append(chars[i - 1])
            if count > 1:
                for digit in str(count):  # Add each digit of the count separately
                    res.append(digit)
            count = 1

    # Append the last character and its count
    res.append(chars[-1])
    if count > 1:
        for digit in str(count):  # Add each digit of the count separately
            res.append(digit)

    # Modify the original chars list in place
    chars[:] = res

    return len(res)

# Example usage
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
new_length = compress(chars)
print(new_length)  # Output: 4
print(chars)  # Output: ['a', 'b', '1', '2']

#time complexity: is O(n) where n is the length of the string. as the function iterates through the string once.
#space complexity: is also O(n) because the result list may grow to store all the characters from the string if there are repeated characters
