

from typing import List
def findOrder(numCourses: int, prerequisites : List[List[int]]) -> List[int]:

    graph = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses

    #step 2: Build the graph and update in-degree
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] +=1

    # step 3: Initialize the queue with courses having indegree 0
    queue = []
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    ## Step 4: Process the queue
    topological_order = []

    while queue:
        current = queue.pop(0)
        topological_order.append(current) # Add to the order

        # Reduce in-degree for all dependent courses
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1 # Decrease in-degree
            if in_degree[neighbor] ==0:
                queue.append(neighbor)

    #step 5: Check if topological sort is possible and detect cycle 

    if len(topological_order) == numCourses:
        return topological_order # valid order found
    else:
        return [] # cycle detected, return empty list

# Example usage:
numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]  # To take course 1, you need to finish course 0, etc.
course_order = findOrder(numCourses, prerequisites)
print("Course Order:", course_order)