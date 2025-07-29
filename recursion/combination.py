#Combination Sum: Find all unique combinations in a set of numbers that sum up to a target number using recursion.

#what is combination?
# combination is selecting objects without considering the order. The formula for combination when selecting r objects from n objects is given by
# c = n!/(n - r)! r!
def combinationSum(candidates, target):
  res = []

  def dfs (i, cur, total):
    #base case 1
    if total == target:
      res.append(cur.copy())
      return
    #base case 2
    if i>= len(candidates) or total > target:
      return

    cur.append(candidates[i])
    dfs(i, cur, total + candidates[i])
    cur.pop()
    dfs(i + 1, cur, total)
  dfs(0, [], 0)
  return res

# Example usage
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))

#time complexity: O(2t) its 2 to the power of t
