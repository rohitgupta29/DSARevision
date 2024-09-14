"""
https://leetcode.com/problems/sequence-reconstruction/description/





"""






from Graphs.topological_sort.recounting_a_sequence_dfs import original_seq, is_unique_dfs


def can_construct_original_seq(original_seq, seqs):

    # Step 1: Build the graph and indegree count
    graph = {}
    in_degree = {}

    #Initialize the graph and in-degree count
    for num in original_seq:
        graph[num] = []
        in_degree[num] = 0


    # Build the graph from the sequences
    for seq in seqs:
        for i in range(len(seq)):
            if seq[i] not in graph:
                graph[seq[i]] = []
                in_degree[seq[i]] = 0

            if i > 0:
                u = seq[i - 1]
                v = seq[i]
                graph[u].append(v) # Add edge from u to v
                in_degree[v] += 1 # Increment in-degree of v

    # Till here, the steps are same. We create a graph and in-degree

    # Step 2: Initialize the queue with nodes of in-degree 0

    queue = []
    for num in in_degree:
        if in_degree[num] == 0:
            queue.append(num) # Start with nodes of in-degree 0

    order = []
    unique_order = True # Flag to check if there's a unique order

    # Step 3: Perform Topological Sort

    while queue:
        if len(queue) > 1:
            unique_order = False # More than one source means multiple orders

        current = queue.pop(0) # Dequeue a node
        order.append(current) # Add it to the topological order

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1 # Decrease in-degree of neighbor

            if in_degree[neighbor] == 0:
                queue.append(neighbor) # Enqueue if in-degree becomes 0

    # Step 4: Check if we could sort all characters

    if len(order) != len(original_seq):
        return False, False # Cannot construct original sequence

    # Step 5: Check if the order matches the original sequence
    if order == original_seq:
        return True, unique_order # can construct and is unique
    else:
        return False, unique_order # cannot construct originalSeq


# Example usage

original_seq = [1,2,3,4]
seqs = [[1,2], [2,3], [3,4]]

can_construct, is_unique = can_construct_original_seq(original_seq, seqs)

print("Can construct Original Sequence: ", can_construct)

print("Is the ordering unique: ", is_unique)