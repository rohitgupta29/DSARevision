import heapq
from typing import List
from collections import defaultdict
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # Djikstra's Algorithm

    graph = defaultdict(list)
    for u, v, time in times:
        graph[u].append((v,time))

    min_times = dict()
    min_heap = [(0, k)] # distance from source to node, node

    # why we are taking heap here?

    while min_heap:
        time_k_to_i, i = heapq.heappop(min_heap)
        if i in min_times:
            continue

        min_times[i] = time_k_to_i
        for nei, nei_time in graph[i]:
            if nei not in min_times:
                heapq.heappush(min_heap, (time_k_to_i + nei_time, nei))

    if len(min_times) == n:
        return max(min_times.values())
    else:
        return -1