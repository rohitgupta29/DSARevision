

def find_max_friendship_value_bfs(n, friendships):

    # Step 1: Initialize the graph
    graph = {}

    # step 2: Build the graph from the friendships
    for u, v in friendships:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)  # Add edge from u to v
        graph[v].append(u)  # Add edge from v to u

    # Step 3: Function to perform BFS and calculate friendship value

    def bfs(start):
        pass