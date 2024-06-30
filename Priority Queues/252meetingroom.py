

## 1. Sort the Interval list
## 2.

from typing import List

data  = [[0,30], [5,10], [15,20]]

def meetingRoom(intervals: List[List[int]]):

    intervals.sort(key= lambda x: x[1])
    print(intervals)
    for i in range(1,len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True

res = meetingRoom(intervals = data)
print(res)