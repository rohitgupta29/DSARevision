

class Graph:

    def __init__(self, matrix):
        self.num_vertices = len(matrix)
        self.adjacency_list = [[] for _ in range(self.num_vertices)]

        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if matrix[i][j] != 0:
                    self.adjacency_list[i].append(j)


    def add_edges(self, source, destination):
        self.adjacency_list[source].append(destination)

    def remove_edge(self, source, destination):
        self.adjacency_list[source].remove(destination)

    def print_graph(self):

        for i in range(self.num_vertices):
            # print the current vertex
            print(f"Vertex {i}: ", end="")
            for neighbor in self.adjacency_list[i]:
                print(f"-> {neighbor}", end="")
            print()

# Example Usage
matrix = [
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0]
]

# Create a graph using the adjacency matrix
graph = Graph(matrix)

graph.print_graph()