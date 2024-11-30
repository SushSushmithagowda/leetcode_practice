#Given a collection of intervals, merge all overlapping intervals

def merge_intervals(intervals):

  intervals.sort(key = lambda i : i[0])
  output = [intervals[0]]

  for start, end in intervals[1:]:
    lastEnd = output[-1][1]


    if start <= lastEnd:
      output[-1][1] = max(lastEnd, end)
    else:
      output.append([start, end])
  return output

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

#time complexity: is O(n log n) as we sort the intervals based on the start times, so n here is the number of intervals
#space complexity: sorting the intervals are done in-place and does not require additional memory. In the worst case, no intervals are merged and the output
# - list will contain all n intervals so it would be O(n)

