"""
Your task is to place eight queens on a chessboard so that no two queens are attacking each other.
As an additional challenge, each square is either free or reserved, and you can only place queens on the free squares.
However, the reserved squares do not prevent queens from attacking each other.

How many possible ways are there to place the queens?

"""

"""
Backtracking Algorithm used: 

1. Initialization: Start with an empty chessboard and an empty set of solutions. 
2. Recursive Function: Define a recursive function, often called 'backtrack' , that 
    attempts to place queens one column at a time. 
3. Base Case: If the current column index is equal to 8 (the total no. of columns), it means 
    all queens have been successfully placed. At this point, record the current arrangement of 
    queens as a valid solution. 
4. Column Iteration: For each column, iterate through each row to try placing the queen:
    - Safety Check: Before placing the queen at position '(row, col)', check if it is safe to do so. 
     This involves ensuring that: 
        - No other queen is in the same row. 
        - No other queen is on the same diagonal (both main and anti-diagonal). 
        
5. Placing the Queen: If the position is safe, place the queen and mark the row and diagonals are occupied. 
6. Recursive Call : Call the 'backtrack' function for the next column (i.e. 'backtrack(col + 1)')  
7. Backtrack: If placing the queen leads to a dead end (i.e. no valid placement for subsequent queens), 
   remove the queen from the current position and mark the row and diagonals are unoccupied. This is backtracking step. 
8. Continue Searching: Continue this process until all columns have been explored. 

"""



def isSafe(board, row, col):
    # check this row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on the left side
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on the left side
        for i, j in zip(range(row, len(board)), range(col,-1, -1)):
            if board[i][j] == 'Q':
                return False

    return True

def solveQueens(board, col):

    if col >= len(board):
        print(board) # A solution is found
        print(len(board))
        return

    for i in range(len(board)):
        if isSafe(board,i,col):
            board[i][col] = 'Q'
            solveQueens(board,col +1) # Recur to place rest of the queens
            board[i][col] = "." # Backtrack


N = 8
board = [['.' for _ in range(N)] for _ in range(N)]

ans = solveQueens(board,0)

print(ans)
