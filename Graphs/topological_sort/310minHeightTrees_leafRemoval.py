"""
https://leetcode.com/problems/minimum-height-trees/description/




Using Leaf Removal Approach
"""

"""
In this approach, we repeatedly remove leaf nodes (nodes with only one edge) until we reach the center(s) of the tree. 


"""


def find_minimum_height_trees(n, edges):
    # Step 1: Handle edge cases
    if n == 1:
        return [0]  # Only one node, return it as the root.

    # Step 2: Initialize the graph and degree count
    graph = {}
    degree = [0] * n # Degree of each node

    # Step 3: Build the graph from the edges
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v) # Increment degree of u
        graph[v].append(u) # Increment degree of v

    # Step 4: Identify all leaf nodes (degree 1)
    leaves = [node for node in range(n) if degree[node] == 1]

    # Step 5: Remove leaf nodes until we have 1 or 2 nodes left
    while n > 2:
        n -= len(leaves) # Reduce the count of nodes
        new_leaves = [] # List to hold new leaves

        # Step 6: Process each leaf
        for leaf in leaves:
            # The leaf has only one neighbor, which is its parent
            neighbor = graph[leaf][0]
            degree[neighbor] -= 1 # Decrease the degree of the neighbor

            # If the neighbor becomes a leaf, add it to new_leaves
            if degree[neighbor] == 1:
                new_leaves.append(neighbor)

        leaves = new_leaves # Update laeves for next iteraton

    return leaves


# Example usage

n = 6
edges = [[0,3], [1,3], [2,3], [4,3], [5,4]]

result = find_minimum_height_trees(n, edges)

print("Minimum Height Trees: ", result)



