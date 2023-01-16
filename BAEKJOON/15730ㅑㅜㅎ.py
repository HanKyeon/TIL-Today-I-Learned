'''
수영장 사장님

물이 고일 수 있는 부분에 물을 채워 넣을 것이다. 얼마만큼 물을 채울 수 있는가?

입력
n, m 제시.
n개 줄 m개의 높이 제시.

출력
최대 물을 채웠을 때 얼마만큼의 물을 채울 수 있는지 출력.
'''
import sys
from collections import deque
input = sys.stdin.readline
'''
이거 저시기로 하자. 딕트로 만들어서 부르자.
'''
def bfs(std):
    global n, m
    q = deque()
    for h, w in bli:
        print( h, w)
        if g[h][w]==std:
            v[h][w] = 1
            ng[h][w] = std
            q.append((h, w))
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw] >= std and not v[nh][nw]:
                v[nh][nw] = 1
                ng[nh][nw] = std
                q.append((nh, nw))


mov = [(-1,0),(0,1),(1,0),(0,-1)]
n, m = map(int, input().rstrip().split())
mh = 0
hmenu = set()
g = []
bli = []
for i in range(n):
    for j in (0, m-1):
        bli.append((i, j))
for i in (0, n-1):
    for j in range(1, m-1):
        bli.append((i, j))

s = list(map(int, input().rstrip().split()))
for j in range(m):
    if s[j] > mh:
        mh = s[j]
    hmenu.add(s[j])
g.append(s)
for i in range(n-2):
    s = list(map(int, input().rstrip().split()))
    for j in range(m):
        if s[j] > mh:
            mh = s[j]
    hmenu.add(s[0])
    hmenu.add(s[-1])
    g.append(s)
s = list(map(int, input().rstrip().split()))
for j in range(m):
    if s[j] > mh:
        mh = s[j]
    hmenu.add(s[j])
g.append(s)
ng = [[mh]*m for _ in range(n)]
hmenu = list(hmenu) # 정렬 해야하나?
hmenu.sort()
while s:
    a = s.pop(0)
    v = [[0]*m for _ in range(n)]
    bfs(a)
for i in ng:
    print(i)

















'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs(h, w):
    global n, m
    ret = 1
    q = deque([(h, w)])
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw]<ng[nh][nw] and not v[nh][nw]:
                ng[nh][nw] -= 1
                v[nh][nw] = 1
                q.append((nh, nw))
                ret += 1
    return ret

n, m = map(int, input().rstrip().split())
g = [list(map(int, list(input().rstrip().split()))) for _ in range(n)]
maxv = max(map(max, g))
ng = [[maxv]*m for _ in range(n)]

a = -1
while a:
    v = [[0]*m for _ in range(n)]
    a = 0
    for i in range(n):
        for j in (0, m-1):
            if g[i][j] == ng[i][j] or v[i][j]:
                continue
            v[i][j] = 1
            ng[i][j] -= 1
            a += bfs(i, j)
    for i in (0, n-1):
        for j in range(1, m-1):
            if g[i][j] == ng[i][j] or v[i][j]:
                continue
            v[i][j] = 1
            ng[i][j] -= 1
            a += bfs(i, j)
for i in ng:
    print(i)
os, ns = sum(map(sum, g)), sum(map(sum, ng))
print(ns-os)
'''





























