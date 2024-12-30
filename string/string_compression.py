#question: String Compression: Implement a method to perform basic string compression using the counts of repeated characters. 
#For example, consider the string "aabbbccc". After compression, it would become "a2b3c3", 
#where the counts of consecutive repeated characters are used to represent the compressed string.

def compressed_string(s):
    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1

    # Append the last character and its count
    result.append(s[-1] + str(count))

    return ''.join(result)

s = "azzzmml"
print(compressed_string(s))

#time complexity: is O(n) where n is the length of the string. as the function iterates through the string once.
#space complexity: is also O(n) because the result list may grow to store all the characters from the string if there are repeated characters
#why efficient? the code efficiently compresses the consecutive repeated chraacters by iterating through once within the string
