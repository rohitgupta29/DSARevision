
from typing import List
from collections import defaultdict
def validPath(n:int, edges: List[List[int]], source: int, destination: int) -> bool:

    # base case
    if source == destination:
        return True

    # create an empty graph
    graph = defaultdict(list)
    # fill graph values with edge values
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # set to hold values
    seen = set()
    seen.add(source)
    stack = [source]

    while stack:
        node = stack.pop()
        if node == destination:
            return True

        for nei_node in graph[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                stack.append(nei_node)

    return False


n = 3
edges = [[0,1], [1,2], [2,0]]
source = 0
destination = 2

ans = validPath(n,edges,source,destination)

print(ans)