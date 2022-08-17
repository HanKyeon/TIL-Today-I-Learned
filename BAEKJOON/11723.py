'''
연결 요소의 갯수

입력
노드갯수N 간선M
간선 시작 끝 M번 제시, 같은 간선 1회만 제시

출력
연결 요소 갯수
'''
import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(num):
    v[num] = 1
    for i in g[num]:
        if v[i] == 0:
            dfs(i)
        else:
            continue

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
v = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
c = 0
for t in range(1, n+1):
    if not g[t]:
        v[t] = 1
        c += 1
    if v[t] == 0:
        dfs(t)
        c+=1
    else:
        continue
print(c)

