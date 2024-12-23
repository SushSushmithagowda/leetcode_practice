#Longest Substring Without Repeating Characters. Find the length of the longest substring without reperating characters.

def length_of_longest_substring(s):
    max_length = 0
    start = 0
    char_index_map = {} #this dictionary stores all the most recent index of each character encountered in the string

    for i, char in enumerate(s): #want to loop through each index and its character in the string
        if char in char_index_map and char_index_map[char] >= start: #it checks if the character is present in the dictionary and the other condition
            start = char_index_map[char] + 1 #adds the encountered character index in the dictionary
        else:
            max_length = max(max_length, i - start + 1)
        char_index_map[char] = i

    return max_length
s = "daffodils"
print(length_of_longest_substring(s))

#Time Complexity: O(n), where n is the length of the string. It iterates only once through the for loop
#Space Complexity: # in the avg case its O(1), 1.is O(n) in the worst case because there are no repeating characters, the dictionary will store atmost n entries. this is because each character in the string will have a correponding entry in the dictionary
# 2.Even in cases where there are repeating characters, the dictionary will still need to store an entry for each character encountered, as it keeps track of the most recent index of each character.
#efficiency? it is concise and efficicent as it uses the sliding window approach to keep track of the current substring without needing to backtrack. Overall the time complexity is O(n) and space complexity is 0(n)
