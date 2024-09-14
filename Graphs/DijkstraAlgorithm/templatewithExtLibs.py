


from collections import defaultdict
import heapq

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edges(self, u, v, weight):
        self.graph[u].append((v,weight)) ## why we have weight inside the brackets


    def dijkstra(self, source):

        dist = {node: float('inf') for node in self.graph}
        dist[source] = 0
        heap = [(0, source)]

        while heap:
            current_dist, current_node = heapq.heappop(heap)

            if current_dist > dist[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))


            return dist


# Example usage

g = Graph()
g.add_edges(0,1,4)
g.add_edges(0,7,8)
g.add_edges(1,2,8)
g.add_edges(1,7,11)
g.add_edges(2,3,7)
g.add_edges(2,8,2)
g.add_edges(2,5,4)
g.add_edges(3,4,9)
g.add_edges(3,5,14)
g.add_edges(4,5,10)
g.add_edges(5,6,2)
g.add_edges(6,7,1)
g.add_edges(6,8,6)
g.add_edges(7,8,7)

source = 0
distances = g.dijkstra(source)

print(f"Vertex \t \t Distance from Source")
for vertex, distance in distances.items():
    print(f"{vertex} \t \t {distance}")



"""

Steps: 

1. Initialize a dictionary 'dist' to store the shortest distances from the source to each vertex. 
Set all distances to infinity initially. 

2. Set the distance of the source vertex to 0. 

3. Create a heap with the source vertex and its distance 0. 

4. While the heap is not empty: 
    - Pop the vertex with the minimum distance from the heap. 
    - If the current distance is greater than the distance storted in dict, skip this vertex. 
    - For each neighbor of the current vertex: 
        - Calculate the distance to the neighbor through the current vertex. 
        - If the calculated distance is shorter than the current distance to the neighbor stored in 'dict': 
            - Update the neighbor's distance in 'dict'. 
            - Push the neighbor and its updated distance to the heap. 
            
5. Return the 'dist' dictionary containing the shortest distances from the source to each vertex. 

TE: O(E log V) , where E = no. of edges and V is no. of vertices in the graph. 
            

"""