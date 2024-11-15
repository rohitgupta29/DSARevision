





def bubbleSort(arr):

    n = len(arr)
    for i in range(n):
        sorted = True
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False
        if sorted == True:
            break
    return arr

arr = [1,4,3,2]
res = bubbleSort(arr=arr)
print(res)



# class Solution:
#     def bubble_sort(self, lst: List[int]) -> None:
#         """
#         Mutates lst so that it is sorted via swapping adjacent elements until
#         the entire lst is sorted.
#         """
#         has_swapped = True
#         # if no swap occurred, lst is sorted
#         while has_swapped:
#             has_swapped = False
#             for i in range(len(lst) - 1):
#                 if lst[i] > lst[i + 1]:
#                     # Swap adjacent elements
#                     lst[i], lst[i + 1] = lst[i + 1], lst[i]
#                     has_swapped = True