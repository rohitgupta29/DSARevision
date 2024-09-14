
from collections import defaultdict
from typing import List
def findOrder(numCourses: int, prerequisites : List[List[int]]) -> List[int]:

    order = []
    graph = defaultdict(list)
    for a,b in prerequisites:
        graph[a].append(b)

    UNVISITED, VISITING, VISITED = 0,1,2
    states = [UNVISITED] * numCourses

    def dfs(i):
        if states[i] == VISITING:
            return False
        if states[i] == VISITED:
            return True
        states[i] = VISITING

        for nei in graph[i]:
            if not dfs(nei):
                return False

        states[i] = VISITED
        order.append(i)
        return True

    for i in range(numCourses):
        if not dfs(i):
            return []

    return order

