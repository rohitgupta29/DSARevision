

def alien_order(words):

    # Step1: Build the graph and in-degree count
    graph = {}
    in_degree = {}

    # Initialize the graph and in-degree count
    for word in words:
        for char in word:
            if char not in graph:
                graph[char] = []
                in_degree[char] = 0


    # Build the graph
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i+1]
        min_length = min(len(word1), len(word2))

        for j in range(min_length):
            if word1[j] != word2[j]:
                graph[word1[j]].append(word2[j]) # Add edge from word1[j] to word[2]
                in_degree[word2[j]] += 1 # Increment in-degree of word2[j]
                break
            else:
                # Check for invalid case where word1 is a prefix of word2
                if len(word1) > len(word2):
                    return ""

    # Step2: Kahn's Algorithm for Topological Sort

    queue = []
    for char in in_degree:
        if in_degree[char] == 0:
            queue.append(char) # Start with characters of in-degree 0

    order = []

    while queue:
        current = queue.pop(0) # Dequeue a character
        order.append(current) # Add it to the topological order

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1 # Decrease in-degree of neighbor
            if in_degree[neighbor] == 0:
                queue.append(neighbor) # Enqueue if in-degree becomes 0

    # Step 3: Check if we could sort all characters
    if len(order) < len(in_degree):
        return "" # Cycle detected or not all characters are included

    return ''.join(order)


# Example usage

words = ["ba","bc","ac", "cab"]

result = alien_order(words)
print("Alien Dictionary Order (Kahn's Algorithm): ", result)


