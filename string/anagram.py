#Given two strings, determine if they are anagrams of each other (contain the same characters with the same frequency). Anagram definition: a word, phrase, or name formed by rearranging the letters of another word

from collections import Counter
def isanagram(str1, str2):
  return Counter(str1) == Counter(str2)

str1 = "animal"
str2 = "iceman"
print(isanagram(str1, str2))

#time complexity: 1. the usage of Counter here counts the frequency of the character in each string taking O(n) and O(m) time so total time complexity is O(m) + O(n) = O(m + n)
# 2.comparing counters - it takes 0(k) where k is the number of unique characters in the string. in the worst case k can be the same as m or n
#space complexity: The space complexity is O(k) for each Counter object, where k is the number of unique characters in the strings.In the worst case, the space complexity can be O(n+m) if the strings have a large number of unique characters.
#how efficient?: 1. using counter from collections leverages efficient built-in functions for counting characters and comparing dictionaries
# 2. if the length of the strings are not the same, the function will quickly determine they are not anagrams without additional computation
