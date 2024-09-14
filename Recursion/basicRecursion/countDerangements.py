
"""
Problem statement
A Derangement is a permutation of ‘N’ elements, such that no element appears in its original position. For example, an instance of derangement of {0, 1, 2, 3} is {2, 3, 1, 0}, because 2 present at index 0 is not at its initial position which is 2 and similarly for other elements of the sequence.

Given a number ‘N’, find the total number of derangements possible of a set of 'N’ elements.

Note:
The answer could be very large, output answer %(10 ^ 9 + 7).

linK: https://www.naukri.com/code360/problems/count-derangements_873861

"""


MOD = 10 **9 + 7


def countDerangements(n):
    # Write your code here.

    countDegrangementRec(n)


def countDegrangementRec(n):

    ## Base condition
    if n == 1:
        return 0

    if n == 2:
        return 1

    return n-1 * countDegrangementRec(n-2) + countDegrangementRec(n-1) % MOD

# Main.

t = int(input())
while t:
    n = int(input())
    print(countDerangements(n))
    t = t-1