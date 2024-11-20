

"""Trapping Rain Water"""

def trap(arr):

    n = len(arr)
    left = []
    right = []
    left[0] = arr[0]

    for i in range(n):
        left[i] = max(left[i-1],arr[i])

    # last element
    right[n-1] = arr[n-1]
    for i in range(0,n-2):
        right[i] = max(right[i+1], arr[i])

    ans = 0

    for i in range(n):
        ans += (min(left[i], right[i]) - arr[i])

    return ans

# res = trap(arr=[4,2,0,3,2,5])
# print(res)


"""Valid Parenthesis"""


def isValid(s):

    stack = []
    brackets = {"(":")", "[":"]", "{":"}"}

    for char in s:
        if char in brackets:
            stack.append(char)
        elif stack and brackets[stack[-1]] == char:
            stack.pop()
        else:
            return False
    return not stack
res = isValid(s="{}()[]")
print(res)