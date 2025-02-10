#Longest Substring Without Repeating Characters:
#Given a string s, find the length of the longest substring without repeating characters.

def longest_substring_no_repeat(s):
  max_length = 0
  start = 0
  char_index_map = {}

  for i, char in enumerate(s):
    if char in char_index_map:
      start = char_index_map[char] + 1

    else:
      max_length = max(max_length, i - start + 1)
    char_index_map[char] = i
  return max_length
