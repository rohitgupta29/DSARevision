
"""Two Sum """
from os import pipe2


def two_sum(arr, target):

    #1.Interate over every possible pair
    for i in range(len(arr)):

        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j

res = two_sum(arr=[1,2,3], target=4)

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

res = twoSum(arr=[1,2,5], target= 7)

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

res = twoSumHash(arr=[1,2,2,4,5], target= 4)

# print(res)


"""167. Tow Sum ii - Input Array is Sorted """

def twoSumii(arr, target):

    numToIndex = {}

    for i in range(len(arr)):
        complement =  target - arr[i]

        if complement in numToIndex:
            return numToIndex[complement] +1, i + 1

        numToIndex[arr[i]] =  i

res = twoSumii(arr=[1,2,3,4], target=3)
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

res = merge(nums1=[1,2,3,0,0,0],m=3, nums2=[2,5,6], n=3)
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


res = generate(numRows=2)
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

res = getRow(rowIndex=3)
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

res = maxProfit(prices=[7,1,3,9,6,4])
# print(res)