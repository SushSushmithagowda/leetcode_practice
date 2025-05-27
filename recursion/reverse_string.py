#Reverse a string using recursion.
# using recursive method
def reverse_string(s):
    if len(s) <= 1: #this is the base case
        return s
    return s[-1] + reverse_string(s[:-1]) #concatenates the last character of the string with the reverse of the substring excluding the last character

# Example usage
s = "hello"
print("Original:", s)
print("Reversed:", reverse_string(s))

#time complexity: is 0(n2) because - a function slices the string s[:-1] which takes O(n) time where n is the length of the string, then it calls reverse_string(s[:-1])
# - which is another slicing and a recursive call
# on the first call, a function slices the string which takes O(n) time and then makes a recursive call, on the second call, the length of the string is (n - 1)
# so a function takes O(n - 1), and then makes a recursive call, this continues until our base case is reached, each time a slicing operaion is made along with
# - the sum of these opertaions and this would be an arithmetic series with a sum of n(n + 1)/2. therefore, the time complexity is O(n2)

#space complexity: for each recursive call, a frame will be added to the call stack, for a string of length n, call stack depth would be O(n)
# each slicing operation creates a new substring of length decreasing by one each time, even though each slicing operation takes O(n) space, a new substring is used
# in the next recursive call and gets garbage collected once that call is done. overall space complexity would be O(n)
