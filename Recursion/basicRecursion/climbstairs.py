
"""
You are climbing a staircase. It takes 𝑁 steps to reach the top.
Each time you can either climb 1 or M steps.
What is the minimum number of climbs you need to do to reach the top, i.e., Nth stair?
"""

def climb(N,M):

    if N == 0:
        return 0

    min_climbs = float('inf')

    # opt1: climb 1 step from N-1
    if N-1 >= 0:
        min_climbs = min(min_climbs, climb(N-1, M) + 1 )
    if N-M >= 0:
        min_climbs = min(min_climbs, climb(N-M, M) + 1)

    return min_climbs


ans = climb(5,2)
print(ans)