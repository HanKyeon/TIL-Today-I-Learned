
a, b = map(int, input().split())

d = []

for i in range(1, 50) :
    j = 1
    while j <= i :
        d.append(i)
        j+=1

print(sum(d[:b]) - sum(d[:a-1]))
