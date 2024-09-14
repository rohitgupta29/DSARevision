
from os import *
from sys import *
from collections import *
from math import *
def topologicalSort(adj, n, e):
    adjlist = [[] for i in range(n)]
    for edge in adj:
        u, v = edge
        if u is not None and v is not None:
            adjlist[u].append(v)
    visited = [False for i in range(n)]
    final_answer = []

    def dfs(node, visited, adjlist):
        visited[node] = True
        for i in adjlist[node]:
            if not visited[i]:
                dfs(i ,visited ,adjlist)
        final_answer.insert(0 ,node)
    for i in range(n):
        if not visited[i]:
            dfs(i ,visited ,adjlist)

    return final_answer