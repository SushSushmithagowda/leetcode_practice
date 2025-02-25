#Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t.

#An isomorphic string is a string whose characters can be replaced in order for it to be the same as string 2 example: s = egg t = add is isomorphic s = foo t = bar is not isomorphic
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_to_t and s_to_t[char_s] != char_t:
            return False
        if char_t in t_to_s and t_to_s[char_t] != char_s:
            return False

        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s

    return True

# Example usage
s = "egg"
t = "add"
print(isIsomorphic(s, t))  # Output: True

s = "foo"
t = "bar"
print(isIsomorphic(s, t))  # Output: False
