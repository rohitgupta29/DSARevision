from collections import deque
from typing import List

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:

    p_que = deque()
    p_seen = set()

    a_que = deque()
    a_seen = set()

    m,n = len(heights), len(heights[0])

    for j in range(n):
        p_que.append((0,j))

    pass 