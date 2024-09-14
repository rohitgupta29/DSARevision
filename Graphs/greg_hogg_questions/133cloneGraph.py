
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Optional["Node"]) -> Optional["Node"]:

    if not node:
        return None

    start = node
    o_to_n = dict()


    visited = set()
    visited.add(start)
    stk = [start]

    while stk:
        node = stk.pop()
        o_to_n[node] = Node(val = node.val)

        for nei in node.neighbors:
            if nei not in visited:
                visited.add(nei)
                stk.append(nei)

    for old_node, new_node in o_to_n.items():
        for nei in old_node.neighbors:
            new_nei = o_to_n[nei]
            new_node.neighbors.append(new_nei)

    return o_to_n[start]


# practice by dry run understanding

adjList = [[2,4], [1,3],[2,4],[1,3]]

res = cloneGraph(node = adjList)

print(res)