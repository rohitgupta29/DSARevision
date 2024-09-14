
import heapq

from typing import List

def minCostConnectPoints(points: List[int]) -> int:

    n = len(points)
    total_cost = 0
    heap = [(0,0)]
    seen = set()

    while len(seen) < n:
        dist, i = heapq.heappop(heap)
        print(dist,i)
        if i in seen:
            continue

        seen.add(i)
        total_cost += dist
        xi, yi = points[i]

        for j in range(n):
            if j not in seen:
                xj,yj = points[j]
                nei_dist = abs(xi-xj) + abs(yi - yj)
                heapq.heappush(heap, (nei_dist, j))

        return total_cost


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
ans = minCostConnectPoints(points)

print(ans)
