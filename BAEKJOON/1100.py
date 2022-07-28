a = []
for i in range(8) :
    a.append(input())

n1 = [0, 2, 4, 6]
n2 = [1, 3, 5, 7]
c = 0
for i in n1 :
    for j in n1 :
        if a[i][j] == 'F' :
            c += 1
for x in n2 :
    for y in n2 :
        if a[x][y] == 'F' :
            c += 1

print(c)