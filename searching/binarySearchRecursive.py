def binarySearchIterative(arr,start,end, target):

    if (start <= end):
        mid = start + end //2
        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return binarySearchIterative(arr,start, mid-1,target)
        else:
            return binarySearchIterative(arr,mid+1,end,target)



arr = [1,2,3,4,5,6,7,8]
target = 4
start = 0
end = len(arr) -1
res = binarySearchIterative(arr,start,end,target)
print(res)
