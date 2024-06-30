
from collections import Counter
import heapq
def frequencySort(s:str) -> str:

    counter = Counter(s)

    pq = [(-freq,char) for char,freq in counter.items()]

    heapq.heapify(pq)
    result = ''
    while pq:
        freq, char = heapq.heappop(pq)
        print(freq,char)
        result += char * -freq
        print(result)
    return result


print(frequencySort(s= "Tree"))