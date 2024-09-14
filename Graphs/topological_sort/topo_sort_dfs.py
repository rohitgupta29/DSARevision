



class Graph:
    def __init__(self):
        self.graph = {} # Adjacency list representation of the graph

    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v) # Add edge from u to v

    def dfs(self, v, visited, stack):
        visited.add(v) # marking the current node as visited
        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph.get(v, []):
            self.dfs(neighbor, visited, stack)
        stack.append(v) # Push current vertex to stack after visiting all neighbors


    def topological_sort_dfs(self):
        visited = set() # set to track visited nodes
        stack = []

        for vertex in self.graph:
            if vertex not in visited:
                self.dfs(vertex, visited, stack)

        return stack[::-1] # Return reversed stack for topological sort


# Example usage
g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(3, 1)
g.add_edge(2, 3)

top_order_dfs = g.topological_sort_dfs()
print("Topological Sort (DFS):", top_order_dfs)