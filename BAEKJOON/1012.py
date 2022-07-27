import sys
sys.setrecursionlimit(10**6)

def dfs(x, y) :
    if x<0 or x>=n or y<0 or y>=m :
        return False
    if d[x][y] == 1 :
        d[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

for t in range(int(input())) :

    n, m, k = map(int, input().split())
    d = [[0] * m for _ in range(n)]
    c = 0

    for _ in range(k) :
        a, b = map(int, input().split())
        d[a][b] = 1
    
    for i in range(n) :
        for j in range(m) :
            if dfs(i, j) == True:
                c+=1
    
    print(c)
