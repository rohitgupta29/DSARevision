"""
Implement Dijkstra's algorithm to find the shortest path between two nodes in a weighted graph.

"""




class MinHeap:

    def __init__(self):
        self.heap = []


    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]

        # Move the last element to the root and bubble down
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def _bubble_up(self, index):

        parent = (index - 1) // 2
        while index > 0 and self.heap[index][1] < self.heap[parent][1]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]

            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][1] < self.heap[smallest][1]:
            smallest = left
        if right < len(self.heap) and self.heap[right][1] < self.heap[smallest][1]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)



class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = {}

    def add_edges(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, weight))


    def dijkstra(self, start, end):

        # Step 1: Initialize distances and priority queue
        dist = {node: float('inf') for node in range(self.V)}
        dist[start] = 0
        min_heap = MinHeap()
        min_heap.insert((start, 0))

        # Step 2: Initialize parent directory to reconstuct the path
        parent = {start: None}

        while min_heap.heap:
            current_node, current_dist = min_heap.extract_min()

            # If we reached the end node, we can stop
            if current_node == end:
                break

            # Step 3: Explore Neighbors
            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_dist + weight

                # if a shorter path to neighbor is found
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    parent[neighbor] = current_node
                    min_heap.insert((neighbor, distance))

        # step 4: Reconstuct the shortest path
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parent.get(current)

        path.reverse()  # Reverse the path to get it from start to end

        return path, dist[end]


# Example usage

g = Graph(6)

g.add_edges(0,1,7)
g.add_edges(0,2,9)
g.add_edges(0,5,14)
g.add_edges(1,2,10)
g.add_edges(1,3,15)
g.add_edges(2,3,11)
g.add_edges(3,4,6)
g.add_edges(4,5,9)

start_node = 0
end_node = 4
path, distance = g.dijkstra(start_node, end_node)

print(f"Shortest path from {start_node} to {end_node} : {path} with distance {distance}")