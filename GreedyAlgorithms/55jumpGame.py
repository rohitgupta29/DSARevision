
from typing import List

def canJump(nums: List[int]):

    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False

        farthest = max(farthest, i + nums[i])

        if farthest >= len(nums) - 1:
            return True

    return False


nums = [2,3,1,1,4]

res = canJump(nums)

print(res)


# ref : https://www.youtube.com/watch?v=OjsmwsdCtX8