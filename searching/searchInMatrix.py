


def searchInMatrix(input, searching):

    if (len(input) == 0):
        return False

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == searching:
                return True
    return False









input = [[1,2,3],[4,5,6],[7,8,9]]

res = searchInMatrix(input=input, searching= 5)

print(res)