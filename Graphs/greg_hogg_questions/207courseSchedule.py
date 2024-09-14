
from collections import defaultdict
from typing import List
def canFinish(numCourses: int, prerequisites: List[List[int]] ) -> bool:

    # prepare a graph
    graph = defaultdict(list)
    courses = prerequisites
    for a,b in courses:
        graph[a].append(b)

    UNVISITED = 0
    VISITING = 1
    VISITED = 2

    states = [UNVISITED] * numCourses

    def dfs(node):
        state = states[node]
        if state == VISITED: return True
        if state == VISITING: return False

        states[node] = VISITING

        for nei in graph[node]:
            if not dfs(nei):
                return False
        states[node] = VISITED
        return True
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True


numCourses = 2
prerequisites = [[1,0]]

ans = canFinish(numCourses, prerequisites)

print(ans)