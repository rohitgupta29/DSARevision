from itertools import cycle


def can_construct_original_seq_dfs(original_seq, seqs):
    # step1: Build the graph and in-degree count
    graph = {}
    in_degree = {}

    # Initialize the graph and in-degree count
    for num in original_seq:
        graph[num] = []
        in_degree[num] = 0


    # Build the graph from the sequence
    for seq in seqs:
        for i in range(len(seq)):
            if seq[i] not in graph:
                graph[seq[i]] = []
                in_degree[seq[i]] = 0

            # now fil the graph and add indegrees
            if i > 0:
                u = seq[i-1]
                v = seq[i]
                graph[u].append(v)  # Add edge from u to v
                in_degree[v] += 1 # Increment in-degree of v

    # step 2: DFS for Topological Sort
    visited = {}
    order = []
    cycle_detected = False

    def dfs(node):
        nonlocal cycle_detected
        if node in visited:
            return visited[node] # Return the state of the node
        visited[node] = False  # Mark as Visiting

        for neighbor in graph[node]:
            if visited.get(neighbor) is False:
                cycle_detected = True
                return
            if neighbor not in visited:
                dfs(neighbor)

        visited[node] = True # Mark as visited
        order.append(node)


    for char in in_degree:
        if char not in visited:
            dfs(char)
            if cycle_detected:
                return False, False # Cycle Detected

    # Step 3: Check if the order matches the original sequence
    order.reverse() # Reverse the order to get the topological sort

    if order == original_seq:
        return True, True
    else:
        return False, False # Cannot construct Original sequence


# Example usage

original_seq = [1,2,3,4]

seqs = [[1,2],[2,3],[3,4]]

can_construct_dfs, is_unique_dfs = can_construct_original_seq_dfs(original_seq, seqs)

print("Can construct original sequence (DFS): ", can_construct_dfs)

print("Is the ordering unique (DFS) : ", is_unique_dfs)




