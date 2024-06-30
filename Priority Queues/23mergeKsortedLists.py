import heapq

data = [[1,4,5], [1,3,4], [2,6]]
def mergeksortedlists(lists):

    heap = []
    for list in range(len(lists)):
        for i in lists[list]:
            heapq.heappush(heap, i)

    return heap


res = mergeksortedlists(lists=data)

print(res)