



def minChanges(s):

    changes = 0
    if len(s) < 2:
        return 0
    if s == len(s) * s[0]:
        return 0

    for i in range(0,len(s)+1, 2):
        if i + 1 < len(s):
            if s[i] != s[i+1]:
                changes += 1

    return changes





res = minChanges(s= "10001001")

print(res)