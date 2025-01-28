#Count and Say: Given an integer n representing the number of terms in the sequence, generate the nth term of the "count and say" sequence.

def count_and_say(n):
    if n == 1:
        return "1"

    prev_term = "1"
    for _ in range(2, n + 1):
        curr_term = ""  # Initialize an empty string for the current term
        count = 1       # Initialize count for consecutive digits
        i = 1           # Start traversing the previous term from index 1

        # Traverse the previous term
        while i < len(prev_term):
            # Count consecutive digits
            if prev_term[i] == prev_term[i - 1]:  # If current digit is same as previous one
                count += 1                         # Increment count
            else:
                # If current digit is different, append count and digit to curr_term
                curr_term += str(count) + prev_term[i-1]
                count = 1  # Reset count to 1 for the new digit
            i += 1       # Move to the next digit in the previous term

        # Append count and last digit to the current term
        curr_term += str(count) + prev_term[-1]

        # Update previous term for next iteration
        prev_term = curr_term

    return prev_term  # Return the nth term
