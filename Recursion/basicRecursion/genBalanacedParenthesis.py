
"""
To generate all balanced parentheses of length
𝑛
n in lexicographic order, we can utilize a backtracking approach.
The key is to ensure that at any point in the string,
the number of closing parentheses does not exceed the number of opening parentheses,
and that we only generate valid combinations.

"""


def generate_parentheses(n):

    def backtrack(current, open_count, close_count):

        if len(current) ==n:
            result.append(current)
            return

        if open_count < n//2:
            backtrack(current + '(', open_count+1, close_count)

        if close_count < open_count:
            backtrack(current + ')', open_count,close_count + 1)

    result = []
    backtrack('',0,0)
    return result

ans = generate_parentheses(4)

print(ans)