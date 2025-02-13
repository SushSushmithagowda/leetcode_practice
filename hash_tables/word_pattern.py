#Given a pattern and a string str, find if str follows the same pattern. Here, "follows" means a full match, such that there is a bijection between a letter in the pattern and a non-empty word in str. Pattern: "abba" String: "dog cat cat dog" In this case, 'a' in the pattern corresponds to "dog", and 'b' corresponds to "cat". Since the pattern and string follow the same bijection, the output would be True
#bijection: a relation between two sets such that each element of either set is paired with exactly one element of the other set
def word_pattern(pattern, string):

  words = string.split()

  if len(pattern) != len(words): #when we split for example "dog cat cat dog" becomes ['dog', 'cat', 'cat', 'dog'] the length = 3 and pattern = "abba" = 3

    return False

  char_to_words = {}
  words_to_char = {}

  #zip works this way - a,dog; b,cat; b.cat; a,dog;
  for char, word in zip(pattern, words):
    if char in char_to_words and char_to_words[char] != word:
      return False
    if word in words_to_char and words_to_char[word] != char:
      return False
    char_to_words[char] = word #if the first condition is not true, this gets executed
    words_to_char[word] = char #if the second condition is not true, this gets executed
  return True
pattern = "abba"
string = "dog cat cat dog"
print(word_pattern(pattern, string))

#time complexity: would be O(n + m) when n is the length of the pattern and m is the length of the string
#space complexity: would be O(n + m) as we have two hash maps - one for pattern and the other for string
