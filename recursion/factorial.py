#Write a function to calculate the factorial of a given number using recursion.

def factorial_num(n):
  if n == 0:
    return 1
  return n * factorial_num(n - 1)

n = 5 #if n is large like 1000 then to handle this we can use a library that supports arbitrary-precision arithmetic such as 'math' module like shown in the next
#code segment
print(factorial_num(n))

#time complexity: is O(n) where n is the input number, this is because the function makes n recursive calls to calculat the factorial of a given number
#space complexity: is also O(n) where n is the input number, because everytime a recursive function is called, it adds a new frame to the stack, and there are
# - n such frames in the worst case

#whereas the iteartive approach takes much lesser space where the space complexity would be O(1) because it uses a constant amount of space regardless of the
# - input size
