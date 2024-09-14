
"""
Problem statement
A Derangement is a permutation of ‘N’ elements, such that no element appears in its original position. For example, an instance of derangement of {0, 1, 2, 3} is {2, 3, 1, 0}, because 2 present at index 0 is not at its initial position which is 2 and similarly for other elements of the sequence.

Given a number ‘N’, find the total number of derangements possible of a set of 'N’ elements.

Note:
The answer could be very large, output answer %(10 ^ 9 + 7).

linK: https://www.naukri.com/code360/problems/count-derangements_873861

"""


def countDerangements(n):

    # create an array for DP

    memo = list()
    memo = [-1 for i in range(n+1)]
    return countDerangementMemo(n, memo)

def countDerangementMemo(n, memo):

    if n==1:
        return 0
    if n ==2:
        return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = (n-1) * (countDerangementMemo(n-2, memo) + countDerangementMemo(n-1,memo))
    return memo[n]