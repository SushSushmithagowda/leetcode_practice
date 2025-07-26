#Merge Sort: Implement the merge sort algorithm using recursion. Divide: Divide the array into two halves, a left half and a right half. Conquer: Recursively sort the left half and the right half. 
#Combine: Merge the two sorted halves into a single

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive calls to divide and conquer
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half, if any
        #if right_half is exhausted but left_half still has elements, i copy the remaining elements from left_half to the arr
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half, if any
        #if left_half is exhausted but right_half still has elements, I copy the remaining elements from right_half to the arr
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)

#time complexity: in the best, worst and avg cases, the array is divided in half each time (log n divisions)
# - each divison requires merging which is O(n) time. therefore the overall time complexity is O(n log n)

#space complexity: is O(n) because it reqires additional space to store temporary arrays during merging
