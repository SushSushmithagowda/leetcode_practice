#Word Break: Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

def wordbreak(s, wordDict):
  dp = [False] * (len(s) + 1)
  dp[len(s)] = True #base case
  for i in range(len(s) -1, -1, -1):
    for w in wordDict:
      #to check if the string has enough characters to compare with the word in the dict
      if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
        dp[i] = dp[i + len(w)]
      if dp[i]:
        break
  return dp[0]
