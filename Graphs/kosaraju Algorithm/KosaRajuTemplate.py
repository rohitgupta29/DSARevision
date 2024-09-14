



class Graph:

    def __init__(self, vertices):
        # step 1: Initialize the graph with a given number of vertices
        self.V = vertices  # node point
        self.adj = [[] for _ in range(vertices)] # Adjaency list for the graph

    def add_edge(self, u, v):
        # Step 2: Add an edge from vertex u to vertex v
        self.adj[u].append(v)

    def dfs(self, v, visited, stack):
        #step3 : Perform DFS and Store vertices in the stack based on finishing times

        visited[v] = True # Mark the current vertex as visited
        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)  # Recur for all the vertices adjacent to this vertex
        stack.append(v) # Push current vertex to stack after all its neighbors are visited

    def transpose(self):
        # step4: Create a transpose graph
        transposed_graph = Graph(self.V) # Initialize a new graph for the transposed version
        for v in range(self.V):
            for neighbor in self.adj[v]:
                transposed_graph.add_edge(neighbor, v) # Reverse the direction of edges

        return transposed_graph

    def dfs_transposed(self, v, visited):
        # Step 5: Perform DFS on the transposed graph and print the SCC
        visited[v] = True #Mark the current vertex as visited
        print(v, end=" ") # Print the vertex in the current SCC

        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self.dfs_transposed(neighbor, visited) # Recur for all the vertices adjacent to this vertex

    def find_sccs(self):
        # Step 6: Main Function to find and print all SCCs
        stack = [] # Stack to hold the finishing order of vertices
        visited = [False] * self.V #Track visited vertices

        # Step 7: Fill the stack with Vertices based on their finishing times

        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Step 8: Create a transposed Graph
        transposed_graph = self.transpose()

        # Step 9: Perform DFS on the transposed graph in the order of stack
        visited = [False] * self.V

        while stack:
            v = stack.pop() # Get the top vertex from the stack
            if not visited[v]:
                # Step 10: Print the current SCC
                print("SCC: ", end = ' ')
                transposed_graph.dfs_transposed(v, visited)  # able to use this function because it is also a graph
                print()  # New line for the next SCC


# Example Usage

if __name__ == "__main__":
    g = Graph(5)  # Create a graph with 5 vertices
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(1,3)
    g.add_edge(3,4)

    print("Strongly Connected Components: ")
    g.find_sccs()  # Find and print all SCCs
