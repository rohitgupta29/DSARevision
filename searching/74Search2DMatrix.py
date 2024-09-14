from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if matrix == None or len(matrix) == 0:
        return False

    # no. of columns
    m = len(matrix[0]) - 1
    # columns
    i = len(matrix) - 1
    j = 0

    while (i >= 0 and j <= m):

        if (target < matrix[i][j]):

            i -= 1
        elif (target > matrix[i][j]):
            j += 1

        else:
            return True

    return False

matrix = [[1,3,5,7],[10,11,16,20]]

res = searchMatrix(matrix= matrix , target= 3)

print(res)