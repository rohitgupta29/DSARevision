

"""
You are climbing a staircase. It takes 𝑁 steps to reach the top.
Each time you can either climb 1 or M steps.
What is the minimum number of climbs you need to do to reach the top, i.e., Nth stair?
"""

def climb(N,M):

    if N == 0:
        return 0

    min_climbs = float('inf')

    # opt1: climb 1 step from N-1
    if N-1 >= 0:
        min_climbs = min(min_climbs, climb(N-1, M) + 1 )
    if N-M >= 0:
        min_climbs = min(min_climbs, climb(N-M, M) + 1)

    return min_climbs


ans = climb(5,2)
# print(ans)




"""
To generate all balanced parentheses of length
𝑛
n in lexicographic order, we can utilize a backtracking approach.
The key is to ensure that at any point in the string,
the number of closing parentheses does not exceed the number of opening parentheses,
and that we only generate valid combinations.

"""


def generate_parentheses(n):

    def backtrack(current, open_count, close_count):

        if len(current) ==n:
            result.append(current)
            return

        if open_count < n//2:
            backtrack(current + '(', open_count+1, close_count)

        if close_count < open_count:
            backtrack(current + ')', open_count,close_count + 1)

    result = []
    backtrack('',0,0)
    return result

ans = generate_parentheses(4)

# print(ans)



"""
Your task is to place eight queens on a chessboard so that no two queens are attacking each other.
As an additional challenge, each square is either free or reserved, and you can only place queens on the free squares.
However, the reserved squares do not prevent queens from attacking each other.
How many possible ways are there to place the queens?
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



"""
Given an array of size 𝑁, and Q queries, for each query,
you need to get the indices of the elements of the array whose subset-sum is equal to the queried sum ,
if possible, else return -1.
"""


def findSubsetSum(arr, n, target_sum, current_indices):

    #Base case: If target_sum is 0, we found a valid subset
    if target_sum == 0:
        return current_indices

    # Base case: if no elements left or target_sum becomes negative
    if n == 0 or target_sum < 0:
        return None

    # Include the last element in the subset
    include_last = findSubsetSum(arr, n-1, target_sum - arr[n-1], current_indices + [n-1])

    if include_last is not None:
        return include_last

    # Exclude the last element from the subset
    exclude_last = findSubsetSum(arr, n-1,target_sum, current_indices)
    return exclude_last


def subsetSum(arr, target_sum):
    n = len(arr)
    result = findSubsetSum(arr,n,target_sum,[])
    if result is not None:
        return result
    else:return -1

# Example usage:
arr= [3,34,4,12,5,2]
target_sum = 9
result = subsetSum(arr, target_sum)

print(result)

