"""
There are 𝑁 items numbered from 1 to 𝑁. The 𝑖𝑡ℎ item has a weight of wi and a value of vi.
You have to choose some items out of the 𝑁 items and carry them home in a knapsack.
The capacity of the knapsack is 𝑊 which donate the maximum weight that can be carried inside the knapsack.
In other words, 𝑊 means the total summation of all weights of items that can be carried in the knapsack.

Print maximum possible sum of values of items that you can take home.
Note: Solve this problem using recursion.

Output Format:
Print maximum possible sum of values of items that you can take home.

Constraints:
1≤T≤10
1≤N≤20
1≤W≤100
1≤w ≤50
1≤vi ≤1000

"""

def knapsack_recursive(weights, values, W, N):
    # Base Case: No items left or capacity is 0
    if N == 0 or W ==0:
        return 0

    # If the weight of the current item is more than the capacity, skip it
    if weights[N-1] > W:
        return knapsack_recursive(weights,values, W, N-1)
    else:
        # Return the maximum of the two cases:
        # 1. Include the current item
        # 2. Exclude the current Item
        include_item = values[N-1] + knapsack_recursive(weights,values, W-weights[N-1], N-1)
        exclude_item = knapsack_recursive(weights,values, W, N-1)
        return max(include_item, exclude_item)


# Example usage
if __name__ == "__main__":
    N = 4  # Number of items
    weights = [2, 3, 4, 5]  # Weights of the items
    values = [3, 4, 5, 6]   # Values of the items
    W = 5  # Capacity of the knapsack

    max_value = knapsack_recursive(weights, values, W, N)
    print("Maximum possible sum of values:", max_value)