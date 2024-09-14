"""
Given an array of size 𝑁, and Q queries, for each query,
you need to get the indices of the elements of the array whose subset-sum is equal to the queried sum ,
if possible, else return -1.
"""


def findSubsetSum(arr, n, target_sum, current_indices):
    """

    :param arr:
    :param n: no. of elements left
    :param target_sum:
    :param current_indices: keeps tracks of the indices of the included elements.
    :return:
    """
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