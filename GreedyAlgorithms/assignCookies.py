
from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:


    g = sorted(g)
    s = sorted(s)
    print(g, s)
    i = 0
    j = 0

    content_children = 0

    while i < len(g) and j < len(s):

        if s[j] >= g[i]:
            content_children += 1
            i += 1
        j += 1

    return content_children


g = [1,2,3]
s = [1,1]

res = findContentChildren(g,s)

print(res)