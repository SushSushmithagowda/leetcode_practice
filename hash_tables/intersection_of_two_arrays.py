#Given two arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays, and the result can be in any order.

from collections import Counter

def intersect(nums1, nums2):
    # Count the frequency of each element in both arrays
    count1 = Counter(nums1)
    count2 = Counter(nums2)

    # Find the intersection of the keys (elements) in both counts
    intersection = count1.keys() & count2.keys()

    # Build the result array by repeating each element according to its frequency in both arrays
    result = []
    for num in intersection:
        result.extend([num] * min(count1[num], count2[num]))

    return result

# Example usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))  # Output: [2, 2]
