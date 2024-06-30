
# Construct a Max heap for [53,50,40,23,30,10,5]

## Inserting in Heap


# minHeap


def insertInMinHeap(queue, element):
    queue.append(element)
    curindex = len(queue) - 1
    while (curindex > 0):
        parent_index = (curindex - 1) // 2
        if queue[curindex] < queue[parent_index]:
            queue[curindex], queue[parent_index] = queue[parent_index], queue[curindex]
            curindex = parent_index
        else:
            break


queue = []
insertInMinHeap(queue, 3)
insertInMinHeap(queue, 3)
insertInMinHeap(queue, 1)
insertInMinHeap(queue, 6)
insertInMinHeap(queue, 5)
insertInMinHeap(queue, 2)
insertInMinHeap(queue, 4)

print(queue)

