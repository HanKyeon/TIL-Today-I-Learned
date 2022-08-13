'''
색종이
'''
import sys
input = sys.stdin.readline

n = int(input())
g = [[0] * 1001 for _ in range(1001)]

for i in range(n):
    x, y, dx, dy = map(int, input().split())
    for k in range(y, y+dy) :
        g[k][x:x+dx] = [i+1]*dx

for i in range(1, n+1):
    c = 0
    for b in g :
        c +=b.count(i)
    print(c)
################################################################
def fn(num):
    c = 0
    for i in range(1001):
        c += g[i].count(num)
    return c

n = int(input())
g = [[0] * 1001 for _ in range(1001)]

for i in range(n):
    x, y, dx, dy = map(int, input().split())
    for j in range(x, x+dx) :
        for k in range(y, y+dy) :
            g[j][k] = i+1

for i in range(1, n+1):
    print(fn(i))