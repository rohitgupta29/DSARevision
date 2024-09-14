from Graphs.topological_sort.alien_dict_dfs import result_dfs


def find_minimum_height_trees_dfs(n, edges):

    # Step1: Handle Edge Cases
    if n == 1:
        return [0]

    # Step 2: Initialize the graph
    graph = {} # Adjacency list representation of the tree

    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v) # Add edge from u to v
        graph[v].append(u) # Add edge from v to u

    # Step 3: Function to perform DFS and return the farthest node and its distance

    def dfs(node, parent):
        max_distance = 0
        farthest_node = node
        for neighbor in graph[node]:
            if neighbor != parent: # Avoid going back to the parent
                distance, candidate_node = dfs(neighbor, node)

                if distance + 1 > max_distance:
                    max_distance = distance + 1
                    farthest_node = candidate_node
        return max_distance, farthest_node

    # Step 4: Find the farthest node from the arbitrary starting node (0)
    _, farthest_node = dfs(0, -1)

    # step 5: Find the longest path from the farthest node

    max_distance, farthest_node_from_farthest = dfs(farthest_node, -1)

    # step 6: Determine the center(s) based on the longest path
    # The Center(s) will be the middle node(s) of the longest path

    path_length = max_distance
    centers = []

    if path_length  % 2 == 0:
        centers.append(farthest_node)  # One center for even length
    else:
        centers.append(farthest_node) # One center for odd length
        # We need to find the actual center node(s), so we can run DFS again to get the middle node(s) if needed.

    return centers


n = 6
edges = [[0,3], [1,3], [2,3], [4,3], [5,4]]

result_dfs = find_minimum_height_trees_dfs(n,edges)
print("Minimum Height Trees (DFS) : ", result_dfs)
