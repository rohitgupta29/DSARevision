
"""
In Heap sort, we heapify our array, and using the max heap, take the largest element being the root of the heap.

We store the root and heapify again the remaining elements.

Store them again and like this, get the sorted array.

possible psudo code:

1. Swap first and last element
2. Heapify it on n - i
3. Repeat 1 and 2


"""

arr = [1,3,2,5,4]

import heapq

# def heapSort(arr):


def heapify(arr, n, i):

    largest = i
    left = 2 * i +1
    right = 2*i + 2

    # here, n is the heap size
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right <n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n//2 -1 , -1, -1):
        print(i)
        heapify(arr,n, i)

    # one by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i , 0)


arr = [9,2,1,7,6,8,5]
heapsort(arr)

print("Sorted Array: ", arr)

for i in range(5,0,-1):
    print("--->",i)