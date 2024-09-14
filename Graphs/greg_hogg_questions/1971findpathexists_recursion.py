
from typing import List
from collections import defaultdict
def validPath(n:int, edges: List[List[int]], source: int, destination: int):
    # 1. DFS with Recursion
    # 2. DFS with Stack (iterative)
    # 3. BFS with Deque

    if source == destination:
        return True

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    seen = set()
    seen.add(source)

    def dfs(i):
        if i == destination:
            return True
        for nei_node in graph[i]:
            if nei_node not in seen:
                seen.add(nei_node)
                if dfs(nei_node):
                    return True

        return False

    return dfs(source)

n = 3
edges = [[0,1], [1,2], [2,0]]
source = 0
destination = 2

ans = validPath(n,edges,source,destination)

print(ans)