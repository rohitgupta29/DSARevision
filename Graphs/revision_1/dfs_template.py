
class Graph:
    def __init__(self, matrix):
        self.num_verices = len(matrix)
        self.adjacency_list = [[] for _ in range(self.num_verices)]

        for i in range(self.num_verices):
            for j in range(self.num_verices):
                if matrix[i][j] != 0:
                    self.adjacency_list[i].append(j)

    def add_edges(self, source, destination):
        self.adjacency_list[source].append(destination)

    def remove_edges(self, source, destination):
        self.adjacency_list[source].remove(destination)

    def print_graph(self):

        for i in range(self.num_verices):
            print(f"Vertex {i}", end="")
            for neighbour in self.adjacency_list[i]:
                print(f"-> {neighbour} ", end="")
            print()

    def dfs_recursive(self,start_vertex):
        # Create a list to track visited Vertices
        visited = [False] * self.num_verices
        print("DFS traversal (recursive) starting from vertex", start_vertex, ":")
        self._dfs_recursive_helper(start_vertex,visited)
        print()

    def _dfs_recursive_helper(self, vertex,visited):
        # Mark the current vertex as visited
        visited[vertex] = True
        print(vertex, end=" ") # print the visited vertex

        # Recur all the vertices adjecent to this vertex
        for adjacent_vertex in self.adjacency_list[vertex]:
            if not visited[adjacent_vertex]:
                self._dfs_recursive_helper(adjacent_vertex,visited)

    def dfs_iterative(self, start_vertex):
        # create a list to track visited vertices
        visited = [False] * self.num_verices
        # Use a stack to keep track of vertices to visit
        stack = []

        # Push the starting vertex onto the stack
        stack.append(start_vertex)
        print("DFS traversal (iterative) starting from vertex", start_vertex, ":")

        while stack:
            # pop a vertex from the stack
            vertex = stack.pop()
            if not visited[vertex]:
                visited[vertex] = True
                print(vertex, end=" ") # Print the visited Vertex

                # Push all unvisited adjacent vertices onto the stack
                for adjacent_vertex in self.adjacency_list[vertex]:
                    if not visited[adjacent_vertex]:
                        stack.append(adjacent_vertex)
        print()


matrix = [
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0]
]


graph = Graph(matrix)

graph.print_graph()

graph.dfs_recursive(0)
graph.dfs_iterative(0)