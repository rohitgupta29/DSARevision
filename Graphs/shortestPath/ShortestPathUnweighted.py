"""
link: https://www.naukri.com/code360/problems/shortest-path-in-an-unweighted-graph_981297


"""



def shortestPath(edges, n, m, s,t):

    # Step1 : Build the graph
    graph = [[] for _ in range(N+1)]

    for u, v in edges:
        graph[u].append