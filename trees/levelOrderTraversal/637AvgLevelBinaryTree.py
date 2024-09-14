class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.item.insert(0,item)
    def dequeue(self):
        if not self.is_empty():
            return self.item.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


def averageOfLevels(root):
    if not root:
        return []
    averages = []

    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty():
        level_sum = 0
        level_count = queue.size()

        for _ in range(level_count):
            node = queue.dequeue()
            level_sum += node.val

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

        averages.append(level_sum/ level_count)

    return averages



abc = [1,2,3]

print(abc[-1].value)
