

arr = [1,2,5,3,5,3]


def mergeSort(arr,start, end):


    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start)//2

        mergeSort(arr, start, mid)
        mergeSort(arr,mid+1, end)
        merge(arr, start,mid,end)
    return arr

def merge(arr,start,mid,end):

    n1 = mid - start + 1
    n2 = end - mid

    left = n1
    right = n2

    # complete later

res = mergeSort(arr,0, end=len(arr) - 1)

print(res)