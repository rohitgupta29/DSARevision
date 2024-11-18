
"""Two Sum """
from os import pipe2

from Recursion.revision import result


def two_sum(arr, target):

    #1.Interate over every possible pair
    for i in range(len(arr)):

        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j

# res = two_sum(arr=[1,2,3], target=4)

# print(res)


def twoSum(arr, target):

    # 1. Interate over every number in the array

    complement = 0
    for i in range(len(arr)):
        if target - arr[i] in arr:
            complement = target - arr[i]
            return i, arr.index(complement)
        # else:
        #     return "!!"

# res = twoSum(arr=[1,2,5], target= 7)

# print(res)

def twoSumHash(arr,target):

    # 1. Create an empty dict
    numToIndex = {}

    # loop through the array and check complement with target - arr[i]
    for i in range(len(arr)):
        complement = target - arr[i]

        # If complement is in the dict, return the needed indices
        if complement in numToIndex:
            return numToIndex[complement], i

        ## Add the current number to our hash table
        numToIndex[arr[i]] = i

# res = twoSumHash(arr=[1,2,2,4,5], target= 4)

# print(res)


"""167. Tow Sum ii - Input Array is Sorted """

def twoSumii(arr, target):

    numToIndex = {}

    for i in range(len(arr)):
        complement =  target - arr[i]

        if complement in numToIndex:
            return numToIndex[complement] +1, i + 1

        numToIndex[arr[i]] =  i

# res = twoSumii(arr=[1,2,3,4], target=3)
# print(res)


"""Merge Sorted Array"""

def merge(nums1,m, nums2, n):

    p1 = m -1
    p2 = n - 1
    p = m + n - 1

    # print(m,n,p)
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -=1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -=1

    while p2 >= 0:
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1

    # print(nums1)

# res = merge(nums1=[1,2,3,0,0,0],m=3, nums2=[2,5,6], n=3)
# print(res)


"""Pascal Triange"""

def generate(numRows):

    triangle = []

    for row in range(numRows):
        new_row = [1] * (row + 1)
        # print("row",row)
        for col in range(1,row):
            # print("working")
            # print("a",triangle[row-1][col - 1])
            # print("b",triangle[row-1][col])
            new_row[col] = triangle[row-1][col-1] + triangle[row - 1][col]

        triangle.append(new_row)

    return triangle


# res = generate(numRows=2)
# print(res)

"""pascal triangle 2"""

def getRow(rowIndex):

    triangle = []
    for row in range(rowIndex):

        new_row = [1] * (row + 1)
        for col in range(1,row):
            new_row[col] = triangle[row-1][col-1] + triangle[row-1][col]
        triangle.append(new_row)
    return triangle[-1]

# res = getRow(rowIndex=3)
# print(res)

"""Buying and Selling Stocks"""

def maxProfit(prices):

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        potential_profit = price - min_price
        if potential_profit > max_profit:
            max_profit = potential_profit

    return max_profit

# res = maxProfit(prices=[7,1,3,9,6,4])
# print(res)


"""buy and sell stocks 2"""


def maxProfit(prices):

    total_profit = 0
    for i in range(len(prices) - 1):
        if prices[i+1] > prices[i]:
            total_profit += prices[i+1] - prices[i]

    return total_profit

# res = maxProfit(prices=[3,4,5,6,2])
# print(res)


"""Majority Element """


def majorityElement(nums):

    candidate = None
    count = 0

    for num in nums:
        if count ==0:
            candidate = num
            count = 1
        else:
            if num == candidate:
                count += 1
            else:
                count -= 1
    return candidate

# res = majorityElement(nums=[3,2,3])

# print(res)

"""Majority Element ii"""

def majorityElement(nums):

    md = {}
    for num in nums:
        md[num] = 0
    for num in nums:
        md[num] += 1

    n2 = []
    for k,v in md.items():
        if v > len(nums)//3:
          n2.append(k)

    return n2

# res = majorityElement(nums= [3,2,3])


"""method 2, majority elements"""

def majorityElements(nums):

    candidate1 = None
    candidate2 = None
    count1 = 0
    count2 = 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        if num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 ==0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    result = []
    for candidate in (candidate1, candidate2):
        if candidate is not None and nums.count(candidate) > len(nums) //3:
            result.append(candidate)

    return result

res = majorityElements(nums= [3,2,3])
# print(res)

nums = [3,2,3]
# print(nums.count(3))

"""Missing Ranges"""


def findMissingRange(nums, lower, upper):

    num_elements = len(nums)

    if num_elements == 0:
        return [[lower, upper]]
    missing_ranges = []

    if nums[0] > lower:
        missing_ranges.append([lower, nums[0] - 1])

    for a,b in zip(nums, nums[1:]):
        # print(a,b )
        if b -a > 1:
            missing_ranges.append([a+1, b-1])
    if nums[-1] < upper:
        missing_ranges.append([nums[-1] + 1, upper])

    return missing_ranges

# res = findMissingRange(nums=[2,5,9,21], lower=0, upper = 30)

# print(res)

"""Alternate Method, missing Ranges"""

def findMissingRanges(nums, lower, upper):

    result = []
    current = lower
    print(".......Hello.............")

    for num in nums:
        if num > current:
            if num == current + 1:
                result.append(current)
            else:
                result.append(f"{current} -> {num - 1}")
        current = num + 1

    if current <= upper:
        if current == upper:
            result.append(f"{current}")
        else:
            result.append(f"{current} -> {upper}")

    return result

res = findMissingRanges(nums=[0,1,3,50,75], lower=0, upper= 99)
# print(res)

