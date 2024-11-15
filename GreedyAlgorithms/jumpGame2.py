


def jumps(nums):

    jumps = 0
    current_end = 0
    farthest = 0
    n = len(nums)

    for i in range(n-1): # no need to jump from the last index
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest # Update the end of the current jump range

    return



