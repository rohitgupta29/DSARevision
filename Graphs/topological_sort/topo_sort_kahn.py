from Graphs.topological_sort.topo_sort_dfs import top_order_dfs


class Graph:

    def __init__(self):
        self.graph = {}  # Adjacency list representation of the graph

    def add_edges(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph: # Ensure the vertex exists in the graph
            self.graph[v] = []
        self.graph[u].append(v)


    def topological_sort_kahn(self):

        in_degree = {u: 0 for u in self.graph} # Initialize the in-degree of each vertex
        # print("in_degree: ", in_degree)

        # Calculate in-degree of each vertex
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] +=1

        print("updated in_degree: ",in_degree)
        # Initiate queue with vertices of in-degree 0
        queue = [u for u in in_degree if in_degree[u] == 0]
        top_order = []

        while queue:
            u = queue.pop(0)
            top_order.append(u) # Add it to topological order

            # Decrease in-degree
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v) # Enqueue if in-degree becomes 0

        # Check if topological sorting is possible (i.e. no cycle)
        if len(top_order) != len(self.graph):
            return "Graph has a cycle, Topological sorting is not possible"


        return top_order



g = Graph()

g.add_edges(5,2)
g.add_edges(5,0)
g.add_edges(4,0)
g.add_edges(4,1)
g.add_edges(3,1)
g.add_edges(2,3)

top_order_kahn = g.topological_sort_kahn()
print("Topological Sort (Kahn's Algorithm) : ", top_order_kahn)