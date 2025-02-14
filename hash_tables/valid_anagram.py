#Valid Anagram: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

THE BEST CODE
def valid_anagram(s, t):

  if len(s) != len(t):
    return False

  countS, countT = {}, {}

  for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i], 0)
    countT[t[i]] = 1 + countT.get(t[i], 0)

  for c in countS:
    if countS[c] != countT.get(c, 0):
      return False
  return True

s = "tea"
t = "eat"

print(valid_anagram(s, t))

#Why?
#time complexity: O(n + m) where n is the length of the string s and m is the length of the string t
#space complexity: O(n + m) as we need extra memeory for both s and t, one downside of this approach is that the usage of extra memory.

#to overcome this memory space we can have an alternate code using Counter from collections pandas library

#to the follow-up question from the interviewer, if asked could you come up with the code that doesnt take much space like O(1) THEN?
#we can use sorted for both s and t and then return True if equals otherwise not. but the space complexity would be for a best case O(1) but the time complexity
# - for good solution would be O(n log n) so you would have to dicuss this with your interviewer. but this solutions is not as efficient compared to the other
# - two solutions
