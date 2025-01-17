#Vaid Parenthesis: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def validparenthesis(s):
  stack = []
  bucket_map = {'[':']', '(':')', '{':'}'}

  for a in s:
    if a in bucket_map: #which means we encountered an opening bracket
      stack.append(a)
    elif a in bucket_map.values(): #which means we encountered a closing bracket
      if not stack:
        return False
      opening_bracket = stack.pop()
      if bucket_map[opening_bracket] != a:
        return False
  return len(stack) == 0
s = "[{]}"
print(validparenthesis(s))

#time complexity: is O(n) where n is the length of the string. Each character is processed once and each push/pop operation is O(1) because each individual stack operation does not depend on the size of the input
#space complexity: is O(n) where n is the length of the string. in the worst case, all characters are opening brackets and are pished on to the stack
