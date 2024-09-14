"""
You're researching friendships between groups of  new college students where each student is distinctly numbered from 1 to n.
At the beginning of the semester, no student knew any other student;
 instead, they met and formed individual friendships as the semester went on.

The friendships between students are: Bidirectional.
If student A is friends with student B, then student B is also friends with student A .
Transitive. If student A is friends with student B and student B is friends with student C, then student A is friends with student C.
In other words, two students are considered to be friends even if they are only indirectly linked through a network of mutual (i.e., directly connected) friends.
The purpose of your research is to find the maximum total value of a group's friendships, denoted by Total.
Each time a direct friendship forms between two students, you sum the number of friends that each of the  students has and add the sum to TOTAL .

You are given  queries, where each query is in the form of an unordered list of  distinct direct friendships between  students. For each query, find the maximum value of  among all possible orderings of formed friendships and print it on a new line.

link: https://www.hackerrank.com/challenges/value-of-friendship/problem
"""


"""
Problem Statement: Given a tree of n nodes labeled from 0 to n - 1,
and an array of n - 1 edges representing friendships, we need to find the maximum value of friendships.
The value of friendships can be calculated based on how many friends each student has. 
"""


def find_max_friendship_value(n, friendships):

    # Step 1: Initialize the graph
    graph = {}

    # Step 2: Build the graph from the friendships
    for u, v in friendships:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v) # Add edge from u to v
        graph[v].append(u) # Add edge from v to u

    # Step 3: Function to perform DFS and calculate friendship value
    def dfs(node, visited):
        visited.add(node) # Mark the node as visited
        total_friends = len(graph[node]) # Count the number of friends for this node

        for neighbor in graph[node]:
            if neighbor not in visited:
                total_friends += dfs(neighbor, visited) # Add friends from the subtree
        return total_friends

    # Step 4: Calculate the maximum friendship value
    max_value = 0
    for student in range(n):
        visited = set()   # Reset visited for each student
        value = dfs(student, visited)  # Calculate the friendship value
        max_value = max(max_value, value)  # Update maximum value

    return max_value


# Example Usage

n = 5
friendships = [(0,1), (1,2), (2,3), (4,3)]
result = find_max_friendship_value(n, friendships)
print("Maximum Friendship Value (DFS): ", result)



