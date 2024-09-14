"""
Given 3 strings s1, s2 and s3, the task is to find the length of the longest common
"""


def LCSof3(s1,s2,s3,i,j,k):
    # Base case : if any of the strings is empty
    if i == 0 or j == 0 or j == 0:
        return 0
    # If the current characters match
    if s1[i-1] == s2[j-1] == s3[k-1]:
        return 1 + LCSof3(s1,s2,s3,i-1,j-1,k-1)

    # If any two characters match
    if s1[i-1] == s2[j-1]:
        return max(LCSof3(s1,s2,s3,i,j,k-1), LCSof3(s1,s2,s3,i-1,j-1,k))
    if s1[i-1] == s3[k-1]:
        return max(LCSof3(s1,s2,s3,i,j-1,k), LCSof3(s1,s2,s3,i-1,j,k-1))
    if s2[j-1] == s3[k-1]:
        return max(LCSof3(s1,s2,s3,i-1,j,k), LCSof3(s1,s2,s3,i,j-1,k-1))

    # If none of the characters match
    return max(LCSof3(s1,s2,s3,i-1,j,k), LCSof3(s1,s2,s3,i,j-1,k))

## Need more understanding