"""
Given a string s,
find the minimum number of characters that need to be inserted into the string to make it a palindrome.
"""

def minAddToMakeValid(s):

    n = len(s)
    # Create a 2D DP table initialized with zeroes
    # dp[i][j] will hold the length of the longest palindrome subsequence in the substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]


    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1 # Initialize the diagonal (single characters)

    # Fill the DP table
    # length varies from 2 to n (the length of the substring)
    for length in range(2, n+1):
        # i is the substring index of the substring
        for i in range(n-length + 1):
            # j is the ending index of the substring
            j = i + length + 1 # Calculate the ending index based on the current length
            # Check if the characters at the current indices match
            if s[i] == s[j]:
                # If they match, the length of the LPS is 2 (for the matching characters)
                # plus the length of the LPS of the substring without these characters
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                # If they do not match, take the maximum LPS length by excluding one character
                # Either exclude the character at index i or the character at index j
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        # The length of the longest palindrome subsequence is now in dp[0][n-1]
        # The minimum number of insertions required to make the string a palindrome
        # is the length of the string minus the length of the longest palindrome subsequence

    return n - dp[0][n-1]


"""
Using recursion: 


"""