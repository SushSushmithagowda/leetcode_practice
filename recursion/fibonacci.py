#Fibonacci: Write a function to calculate the nth Fibonacci number using recursion.
#what is a fibonacci number?
# A fibonacci number is a part of a sequence of numbers where each number is the sum of the preceding ones, usually starts with 0 and 1. This sequence is called
# - a fibonacci number
def fibonacci_num(n):
  #identify the base case
  if n <= 1:
    return n
  else:
    return fibonacci_num(n - 1) + fibonacci_num(n - 2)

n = 5
print(f"the fibonacci number of {n} is {fibonacci_num(n)}")

#time complexity: is O(2^n) where n is the input number, the reason why its this is 'cause for example n=4, the total function calls is 8, for n=5 the function calls
# - is 16 and n=6 its 25, so this exponential increase in the number of calls is why the recursive approach is considered O(2^n)
#space complexity: is O(n) where n is the input number, and its 'caue of the recursive calls and the stack frames
#efficiency: The recursive approach is simple but inefficient for large values of n because it recalculates the Fibonacci numbers for smaller
# - values multiple times. This leads to redundant calculations and slower performance compared to more efficient methods like iterative or
# - memoization-based approaches.
