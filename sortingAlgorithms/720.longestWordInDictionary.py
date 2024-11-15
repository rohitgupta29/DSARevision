def longestWord(words):
    # Convert the list of words into a set for faster lookup
    word_set = set(words)

    # Initialize a variable to hold the longest word
    longest_word = ""

    # Sort the words list. Sorting ensures that we check shorter words first.
    words.sort()

    # Iterate through each word in the sorted list
    for word in words:
        # Check if the word can be formed from its prefix
        # A word can be a candidate only if its prefix (word[:-1]) exists in the set
        # or if the word is of length 1 (single character)
        if len(word) == 1 or word[:-1] in word_set:
            # If the current word is longer than the longest_word found so far
            if len(word) > len(longest_word):
                longest_word = word  # Update the longest_word
            elif len(word) == len(longest_word):
                # If they are of equal length, choose lexicographically smaller one
                longest_word = min(longest_word, word)

    # Return the longest word found
    return longest_word


# Example usage:
# words = ["w", "wo", "wor", "word", "war", "warrior", "a", "ap", "app"]
# print(longestWord(words))  # Output: "word"


# Example input: list of words
words = ["w", "wo", "wor", "world", "war"]

# Call the longestWord function and store the result
result = longestWord(words)

# Print the longest word that can be built from other words
print(result)  # Output: "world"