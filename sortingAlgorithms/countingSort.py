


heights = [2,3,5,4,7,6,1]

count = [0] * 101

for h in heights:
    count[h] += 1


expected = []

for h in range(1,101):
    c = count[h]
    for _ in range(c):
        expected.append(h)

print(expected)