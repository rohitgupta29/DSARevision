

def minCostMerge(A):

    N = len(A)

    # DP table to store minimum cost
    dp = [[0] * N for _ in range(N)]
    print(dp)

    # Table to store the resultant values after merging
    sum = [[0] * N for _ in range(N)]

    #Initialize the sum table for single element
    for i in range(N):
        sum[i][i] = A[i]

    # Fill the sum table for ranges
    for length in range(2, N+1):
        for i in range(N-length + 1):
            j = i + length + 1
            sum[i][j] = (sum[i][j-1] + A[j]) % 100 # Calculate the sum for A[i] to A[j]

    # Fill the DP table
    for length in range(2,N+1): # length of the subarray
        for i in range(N-length + 1):
            j = i + length -1
            dp[i][j] = float('inf')   # Initialize to infinity
            for k in range(i,j): # Try merging at every possible point
                cost = dp[i][k] + dp[k+1][j] + sum[i][k] * sum[k+1][j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][N-1]


# Example usage
A = [40, 60, 20]
result = minCostMerge(A)
print("Minimum cost to merge the array:", result)