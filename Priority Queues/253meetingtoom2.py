

import heapq
from typing import List
def minMeetingRooms(intervals: List[List[int]]) -> int:

    if not intervals:
        return 0
    intervals.sort(key= lambda x: x[0])

    min_heap = []
    heapq.heappush(min_heap, intervals[0][1])

    for i in range(1, len(intervals)):

        if min_heap[0] <=  intervals[i][0]:
            heapq.heappop(min_heap)

        heapq.heappush(min_heap, intervals[i][1])

    return len(min_heap)


result = minMeetingRooms([[0,30], [5,10], [15,20], [5,30]])

print(result)