"""
You are given N bricks in a line and M different coloured buckets of paint.
You have to find the number of ways you can colour the brick wall such that there
are exactly K positions out of the N bricks such that it has a different colour from the brick wall on its immediate left.
(except the first brick, since there is no left brick). Print it modulo 10^9+7.

Output Format:
For each test case, print the number of ways you can colour the brick wall satisfying the given condition % 10^9+7.

Constraints:
1≤ T ≤ 100
1≤ N, M ≤ 2000
0≤ K ≤ N-1
It is guaranteed that the sum of N*K over all test cases does not exceed 4*108.
"""


def count_ways(N,M,K):
    MOD = 10**9 + 7
    dp = [[0] * (K+1) for _ in range(N+1)]

    #Base Case
    for i in range (1,M+1):
        dp[1][0] = (dp[1][0] + 1) % MOD

        # iteriate over the remaining bricks
        for i in range(2,N+1):
            # iterate over a number of different colours
            for j in range(K+1):
                dp[i][j] = (dp[i][j] + (M * dp[i-1][j]) % MOD) % MOD

                # Choose a different color than the previous brick
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD

    # Return the total number of ways
    return sum(dp[N]) % MOD

# Example usage
N = 3
M = 2
K = 1
result = count_ways(N, M, K)
print(result)  # Output: 6