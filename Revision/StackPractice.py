

"""Trapping Rain Water"""
from inspect import stack


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
# print(res)

"""Decode String"""

def decodeString(s):

    stack = []
    curNum = 0
    curString = ""
    for char in s:
        if char == '[':
            stack.append(curString)
            stack.append(curNum)
            print("a", stack)
            curString = ""
            curNum = 0
        elif char == ']':
            num = stack.pop()
            prevString  = stack.pop()
            curString = prevString + num * curString
        elif char.isdigit():
            curNum = curNum * 10 + int(char)
            print("b",curNum)
        else:
            curString += char
    return curString

# res = decodeString(s="3[a]2[bc]")

def decodeString(s):

    stack = []

    for char in range(len(s)):
        if s[char] != "]":
            stack.append(s[char])
        else:
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr
            stack.pop()
            k = ''
            while stack and stack[-1].isdigit():
                k = k + stack.pop()
            stack.append(int(k) * substr)

    return "".join(stack)


# res = decodeString(s= "2[a]3[b]")
# print(res)

"""min stack"""


"""Remove all Adjacent Duplicates in String"""

def removeDuplicates(s):

    stk = []

    for char in s:
        if stk and stk[-1] == char:
            stk.pop()
        else:
            stk.append(char)

    return "".join(stk)

# res = removeDuplicates(s="abbaca")
# print(res)

"""Implement Stack using Queues"""


class MyStack:

    def __init__(self):
        self.que1 = []
        self.que2 = []

    def push(self, x: int) -> None:
        self.que2.append(x)

        while self.que1:
            self.que2.append(self.que1.pop(0))
        self.que1, self.que2 = self.que2, self.que1

    def pop(self) -> int:
        val = self.que1[-1]
        del self.que1[-1]
        return val

    def top(self) -> int:
        return self.que1[-1]

    def empty(self) -> bool:
        return len(self.que1) == 0



"""Next Smaller Element"""
"""https://www.geeksforgeeks.org/problems/immediate-smaller-element1142/1"""




"""Largest Rectangular Question in Histogram"""

def largestRectangleArea(heights):

    stack = []
    max_area = 0

    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            print("big_stack", stack)
            print(str(heights[i]) + " < " + str(heights[stack[-1]]))
            h = heights[stack.pop()]
            print("h", h)
            w = i if not stack else i - stack[-1] - 1
            print("w",w)

            max_area = max(max_area, h*w)
            print("max_area", max_area)

        stack.append(i)
        print('stack', stack)

    # Process remaining bars in the stack
    while stack:
        height = heights[stack.pop()]
        print("h1",height)
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        print("w1", width)
        max_area = max(max_area, height * width)
        print("mArea",max_area)
    return max_area

# res = largestRectangleArea(heights=[2,1,5,6,2,3])
# print(res)


"""Make the string great"""

def stringGreat(input):

    stack = []
    i = 0

    while i < len(input):
        if (stack and stack[-1] != input[i] and stack[-1].lower() == input[i].lower()):
            stack.pop()
        else:
            stack.append(input[i])
        i += 1


    return "".join(stack)

res = stringGreat(input= "leEeetcode")
print(res)