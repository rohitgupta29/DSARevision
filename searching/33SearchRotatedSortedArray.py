


"""
Rotated array:

arr = [0,1,2,4,5,6,7]

rotated = [4,5,6,7,0,1,2]

This one is rotated at index 3, after value 7 we can see the change.

"""



def search(nums, target):

    start = 0
    end = len(nums) -1

    while (start <= end):
        mid = start + (end - start) //2

        if nums[mid] == target:
            return mid

        if nums[start] <= nums[mid]:
            if (target < nums[start]) or target > nums[mid]:
                start = mid + 1
            else:
                end = min -1
        else:
            if (target > nums[end] or target < nums[mid]):
                end = mid -1
            else:
                start = mid + 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 4

res = search(nums, target)

print(res)