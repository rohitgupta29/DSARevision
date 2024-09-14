"""
Given two strings. The task is to find the length of the longest common substring.
"""


def longestCommonSubstring(s1,s2):

    def lcs_helper(i,j,count):
        #Base case : if we reach the end of either string
        if i == len(s1) or j == len(s2):
            return count

        # If characters match, increment count and move to the next characters
        if s1[i] == s2[j]:
            count = lcs_helper(i+1, j+1, count +1)

        # If characters do not match, reset count and check next indices
        count = max(count, lcs_helper(i+1,j,0), lcs_helper(i, j+1, 0))

        return count

    max_length = 0

    # Iterate through each character in both strings to find the longest common substring
    for i in range(len(s1)):
        for j in range(len(s2)):
            max_length = max(max_length, lcs_helper(i,j,0))

    return max_length


# Example usage
s1 = "abcde"
s2 = "abfce"
result = longestCommonSubstring(s1, s2)
print("Length of the longest common substring:", result)