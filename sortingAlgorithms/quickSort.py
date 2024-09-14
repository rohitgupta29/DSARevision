

"""

1. Select a Pivot
2. Move everything smaller than pivot on the left part of pivot
3. move everything larger than pivot on the right part of the pivot

4.

"""


def quickSort(arr,low,high):

    if low < high:

        pi = partition(arr, low,high)

        quickSort(arr,low, pi -1 )
        quickSort(arr, pi+1,high)


def partition(arr,low,high):

    pivot = arr[high]
    i = low - 1

    for j in range(low,high):

        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


arr = [1,4,5,2,4,3]

res = quickSort(arr, 0, len(arr) - 1)

print(res)