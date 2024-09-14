





def count_ways_recursive(n, m, k, prev_color, memo):
    #Base Case
    if n ==0:
        return 1 if k == 0 else 0
    if k <0:
        return 0
    if (n,k,prev_color) in memo:
        return memo[(n,k,prev_color)]

    # If we paint the current brick the same color as previous one
    same_color = count_ways_recursive(n-1, m, k, prev_color, memo)

    # If we paint the current brick a different color
    different_color = count_ways_recursive(n-1,m,k-1,-1,memo) * (m-1) # we reduce the count of k by 1 and choose from 'm-1' colors.

    # total ways
    total_ways = (same_color + different_color) % (10**9 + 7)

    # store the result in the memo dictionary
    memo[(n,k,prev_color)] = total_ways
    return total_ways

def count_ways(N,M,K):
    memo = {}
    return count_ways_recursive(N,M,K,-1, memo)


# Example usage
N = 3
M = 2
K = 1
result = count_ways(N, M, K)
print(result)  # Output: 4