





def selectionSort(arr):

    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [1,3,5,3,5,4]

res = selectionSort(arr)
print(res)