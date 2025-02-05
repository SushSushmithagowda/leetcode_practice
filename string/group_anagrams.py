#Given an array of strings, group anagrams together.

def group_anagrams(input_list):
    anagrams_dict = {}

    # Iterate through each string in the input list
    for string in input_list:
        # Sort the characters of the string and use it as a key
        sorted_string = ''.join(sorted(string)) #the reason why we use joinis because when sorted is applied to lets say tea -> ['a', 'e', 't'] so in order make these chracater into a single
        #string we use join operation

        # If the sorted string is already a key in the dictionary, append the string to its value list
        if sorted_string in anagrams_dict:
            anagrams_dict[sorted_string].append(string)
        # If the sorted string is not a key, create a new key-value pair
        else:
            anagrams_dict[sorted_string] = [string] #why in brackets? becuase we are creating a list of anagram values otherwise, it would be like we are assigning a different value to the key which we dont want

    # Return the values of the dictionary, which are lists of anagrams
    return list(anagrams_dict.values())

# Example usage:
input_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(group_anagrams(input_list))

#time complexity: n is the number of strings and k is the length of each string, so it is O(n.k log k) for sorting each string and processing the list
#space complexity: O(n.k) because each string is stored in the dictionary, and in the worst case we store all strings
#efficiency?: it is efficient as it leverages both hashing and sorting and the use of dictionaries ensures efficient usage of space
