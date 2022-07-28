
d = [64, 32, 16, 8, 4, 2, 1]
x = int(input())
c = 0
for i in d :
    if i <= x :
        c += 1
        x -= i
    if x == 0 :
        print(c)
        break
