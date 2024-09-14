



def alien_order_dfs(words):

    # Step 1: Build the graph and in-degree count
    graph = {}
    in_degree = {}

    # Initiate the graph and in-degree count
    for word in words:
        for char in word:
            if char not in graph:
                graph[char] = []
                in_degree[char] = 0

    # Build the graph
    for i in range(len(words) -1):
        word1 = words[i]
        word2 = words[i+1]
        min_length = min(len(word1), len(word2))

        for j in range(min_length):
            if word1[j] != word2[j]:
                graph[word1[j]].append(word2[j]) # Add edge from word1[j] to word2[j]
                in_degree[word2[j]] += 1  # Increment in-degree of word2[j]
                break
            else:
                    # Check for invalid cases where word1 is a prefix of word2
                if len(word1) > len(word2):
                    return ""


    # Step2 : DFS for Topological Sort
    visited = {}
    order = []
    cycle_detected = False


    def dfs(node):
        nonlocal cycle_detected
        if node in visited:
            return visited[node] # Return the state of the node
        visited[node] = False # Mark as visiting

        for neighbor in graph[node]:
            if visited.get(neighbor) is False: # cycle detected    # Check in detail, get more explaination
                cycle_detected = True
                return
            if neighbor not in visited:
                dfs(neighbor)

        visited[node] = True # Mark as visited
        order.append(node)

    for char in in_degree:
        if char not in visited:
            dfs(char)
            if cycle_detected:
                return ""


    return ''.join(reversed(order))


# Example usage
words = ["ba", "bc", "ac", "cab"]
result_dfs = alien_order_dfs(words)
print("Alien Dictionary Order (DFS):", result_dfs)