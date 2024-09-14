

from collections import defaultdict
from collections import deque
def validPath(n, edges, source, destination):

    if source == destination:
        return True

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    seen = set()
    seen.add(source)
    q = deque()
    q.append(source)

    while q:
        node = q.pop()
        if node == destination:
            return True
        for nei_node in graph[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                q.append(nei_node)

    return False


n = 3
edges = [[0,1], [1,2], [2,0]]
source = 0
destination = 2

ans = validPath(n,edges,source,destination)

print(ans)