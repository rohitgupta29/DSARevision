
"""

"""


def binarySearchIterative(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + (end)) //2    # to avoid the overflow

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid -1 # as mid > target, i.e. target is smaller. So, we will set end as mid -1 as mid is also greater.

    return -1


arr = [1,2,3,4,5,6,7,8]
target = 4

res = binarySearchIterative(arr,target)
print(res)
