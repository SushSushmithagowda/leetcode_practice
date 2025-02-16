#Subarray Sum Equals K:
#Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals k.

#The input nums = [3, 4, 7, 2, -3, 1, 4, 2] k = 7 output = 4 because the subarrays that sum up to 7 are [3, 4], [7], [7, 2, -3, 1], and [1, 4, 2].

def subarraySum(nums, k):
    count = 0
    sum_so_far = 0
    sum_counts = {0: 1}  # stores the count of cumulative sums encountered so far

    for num in nums:
        sum_so_far += num
        if sum_so_far - k in sum_counts:
            count += sum_counts[sum_so_far - k]
        if sum_so_far in sum_counts:
            sum_counts[sum_so_far] += 1
        else:
            sum_counts[sum_so_far] = 1

    return count

# Example usage
nums = [1, -1, 1, 1, 1, 1]
k = 3
print(subarraySum(nums, k))  # Output: 4

#time complexity: O(n) where n is the length of the array, the code iterates through the nums once, performing constant time operation for each element
#space complexity: O(n) because the sum_count dictionary can stor upto n distinct cummulative sums in the worst case scenario where all elements are different and
# and the cummulative sum at each point is unique
#efficiency? uses hash maps to store the cummulative sums found so far, which allows for constant time lookups, this enables the function to determine the
#the contiguous subarrays without needing to iterate through all possible subarrays resulting in faster solutrions compared to brute force approach
