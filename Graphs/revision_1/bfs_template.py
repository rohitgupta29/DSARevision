
class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        #create an adjacency list to store the graph
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, source,destination):
        #Add an edge from source to destination
        self.adjacency_list[source].append(destination)
        # if it is an undirected graph, add this
        self.adjacency_list[destination].append(source)

    def bfs(self, start_vertex):
        # Create a list to track visited vertices
        visited = [False] * self.num_vertices
        # create a list to use as a queue for BFS
        queue = []

        # Mark the start vertex as visited and enqueue it
        visited[start_vertex] = True
        queue.append(start_vertex)

        print(f"BFS traversal starting from vertex {start_vertex}")

        #while there are vertices to process in the queue
        while queue:
            #Dequeue a vertex from the queue
            vertex = queue.pop(0)
            print(vertex,end=" ")

            # Iterate through all adjacent vertices
            for adjacent_vertex in self.adjacency_list[vertex]:
                # If the vertex has not been visited, mark it and enqueue it
                if not visited[adjacent_vertex]:
                    visited[adjacent_vertex] = True
                    queue.append(adjacent_vertex)

        print("") # print a new line after BFS traversal

if __name__ == "__main__":
    # Create a graph with 6 vertices
    graph = Graph(6)

    # Add edges to the graph
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    graph.add_edge(2,5)
    graph.add_edge(2,4)

    # Perform BFS starting from vertex 0
    graph.bfs(0)