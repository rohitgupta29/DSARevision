"""

Approach:

1. We have an array: [2,3,2,5,6]
2. Since it is a circular array, if we include 2, we cant include 6 and vice versa.
- We can use the array as [2,3,2,5] and [3,2,5,6] to handle this. Apply House Robber 1 approach and get max out of
both the solutions using House Robber 1 approach.

"""

## Recursive Approach:

def rob(nums):
    n = len(nums)

    if n == 1:
        return nums[0]

    rob1 = robHelper(nums,0,n-2) # not including the first element

    rob2 = robHelper(nums,1,n-1) #

    return max(rob1, rob2)


def robHelper(nums, start, end):

    if start > end:
        return 0

    if start == end:
        return nums[start]

    robCurrent = nums[start] + robHelper(nums, start + 2, end)
    skipCurrent = robHelper(nums, start + 1, end)

    return max(robCurrent, skipCurrent)


nums = [2,3,2]

a = rob(nums)
print(a)

## Try Memoization and Tabulation





"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums,index):
            if index >= len(nums):
                return 0
            if index in self.memo:
                return self.memo[index]
            lindex = nums[index] + helper(nums,index+2)
            rindex = helper(nums,index+1)
            self.memo[index] = max(lindex,rindex)
            return self.memo[index]
        if len(nums) == 1:
            return nums[0]
        self.memo = {}
        a1 = helper(nums[1:],0)
        self.memo = {}
        b1 = helper(nums[:-1],0)
        return max(a1,b1)

"""