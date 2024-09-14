


class Graph:

    def __init__(self, vertices):
        # step 1: Initialize the graph with given no. of vertices
        self.V = vertices # No. of vertices
        self.adj = [[] for _ in range(vertices)] # Adjacency list for the graph

    def add_edge(self, u, v):
        # Step 2: Add an edge from vertex u to vertex v
        self.adj[u].append(v)

    def dfs(self, v, visited, stack):
        # step 3: Perform DFS and store vertices in the stack based on finishing times
        visited[v] = True # Mark the current vertex as visited