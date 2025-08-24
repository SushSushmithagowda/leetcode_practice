#N-Queens Problem: Find all possible arrangements of N queens on an N×N chessboard such that no two queens attack each other using recursion.

def solveNQueens(n):
  col = set()
  posDiag = set()
  negDiag = set()

  res = []
  board = [["."] * n for i in range(n)] #determine how many rows we are gonna have?

  def backtrack(r): #define a backtracking function that tries to place a queen in the 'r' th row
    if r == n: #the base case - if r == n, all queens are placed, and we have a valid solution
      copy = ["".join(row) for row in board] #convert the board configuration to a list of strings and append it to "res"
      res.append(copy)
    for c in range(n): #iterate through each column in the current row
      if c in col or (r + c) in posDiag or (r - c) in negDiag: #check if placing a queen at either of these positions conflicts with another queen, if yes then skip to the next column
        continue

      col.add(c) #if placing the queen is safe then here we update the sets - col, posDiag, negDiag
      posDiag.add(r + c)
      negDiag.add (r - c)
      board[r][c] = "Q" #we mark the position on the board as a 'Q'

      backtrack(r + 1) #recur to the next row by calling this

      col.remove(c)
      posDiag.remove(r + c)
      negDiag.remove (r - c)
      board[r][c] = "."
  backtrack(0)
  return res

n = 4
print(solveNQueens(n))
