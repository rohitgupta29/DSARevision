"""
Given an undirected and disconnected graph G(V, E), containing 'V' vertices and 'E' edges, the information about edges is given using 'GRAPH' matrix, where i-th edge is between GRAPH[i][0] and GRAPH[i][1]. print its DFS traversal.

V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.

E is the number of edges present in graph G.
Note :
The Graph may not be connected i.e there may exist multiple components in a graph.

Note: Make it work on the website too.
"""


def depth_first_search(v, e, edges):
    # Create an adjacency list to represent the graph
    adj_list = [[] for _ in range(v)]

    # Build the adjacency list from the edges
    for edge in edges:
        source = edge[0]
        destination = edge[1]
        adj_list[source].append(destination)
        print("adj_list_sd: ", adj_list)
        adj_list[destination].append(source)
        print("adj_list_ds: ", adj_list)

    # List to keep track of visited vertices
    visited = [False] * v

    # List to store all components found in the graph
    components = []

    # Perform DFS for each vertex
    for i in range(v):
        if not visited[i]:  # If the vertex is not visited
            component = []  # Create a new component
            dfs(i, adj_list, visited, component)  # Call DFS
            components.append(sorted(component))  # Sort the component and add to components list

    return components


def dfs(node, adj_list, visited, component):
    # Mark the current node as visited
    visited[node] = True
    component.append(node)  # Add the node to the current component

    # Traverse the neighbors of the current node
    for neighbor in adj_list[node]:
        if not visited[neighbor]:  # If the neighbor is not visited
            dfs(neighbor, adj_list, visited, component)  # Recursively call DFS for the neighbor


# Example usage
if __name__ == "__main__":0.

    # Sample input
    v = 5  # Number of vertices
    e = 4  # Number of edges
    edges = [
        [0, 2],
        [0, 1],
        [1, 2],
        [3, 4]
    ]

    # Call the function to perform DFS
    components = depth_first_search(v, e, edges)

    # Print the number of components
    print(len(components))
    # Print each component
    for component in components:
        print(" ".join(map(str, component)))