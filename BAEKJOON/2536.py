'''
버스 갈아타기

2차원 평면상에 m개의 수직선과 n개의 수평선으로 이루어진 격자 형태의 도로망.
시작 좌하단 1,1 우상단 m, n -> 그대로 짜고 돌려서 생각하면 될듯.
운행버스 k개. 버스는 직선으로 운행한다. 각 정점마다 멈춘다.
버스로만 가려고 한다. 이용하려는 버스의 최소 숫자는?

입력
수직선의 수 m과 수평선의 수 n 제시. 1이상 10만이하.
버스의 수 k 제시.
버스 운행구간 제시. 버스 번호, 시작x,y 도착x,y
출발x, y 도착 x, y
출발과 도착은 다르다.

출력
최소 버스 수
'''

from collections import deque
import gc
from heapq import heappop, heappush
import sys
input = sys.stdin.readline


m, n = map(int, input().split())
k = int(input())
g = [set() for _ in range(k+1)]
for _ in range(k):
    i, sh, sw, eh, ew = map(int, input().rstrip().split())
    sh, sw, eh, ew = min(sh, eh), min(sw, ew), max(sh,eh), max(sw, ew)
    g[i].add((sh, sw))
    g[i].add((eh, ew))
    j = 1
    if sh == eh:
        while sw+j < ew:
            g[i].add((sh, sw+j))
            j+=1
    if sw == ew:
        while sh+j < eh:
            g[i].add((sh+j, sw))
            j+=1
sh, sw, eh, ew = map(int, input().rstrip().split())
# for i in g:
#     print(*i)
del m
del n
gc.collect()
r = [[] for _ in range(k+1)]
sta, end = set(), set()
for i in range(1, k+1):
    if (sh, sw) in g[i]:
        sta.add(i)
    if (eh, ew) in g[i]:
        end.add(i)
    for j in range(i, k+1):
        if i == j:
            continue
        if g[i] & g[j]:
            r[i].append(j)
            r[j].append(i)
del g
gc.collect()

q = deque()
v = [0]*(k+1)
ans = int(10e9)
for i in sta:
    q.append(i)
    v[i] = 1
while q:
    i = q.popleft()
    for j in r[i]:
        if v[j] == 0:
            v[j] = v[i]+1
            q.append(j)
for i in end:
    ans = min(ans, v[i])
print(ans)


'''
힙으로 사용한거인데 bfs로 해도 될듯?

heap = []
for i in sta:
    heappush(heap, (1, i, set([i])))
fla = True
ans = int(10e9)
while fla and heap:
    c, idx, v = heappop(heap)
    if idx in end:
        ans = c
        break
    for i in r[idx]:
        if not i in v:
            heappush(heap, (c+1, i, v|{i}))
        if i in end:
            fla = False
            ans = c+1
print(ans)
'''
'''
bfs가 더 빨리 터지네?

ans = int(10e9)
for i in sta:
    q = deque()
    v = [0]*(k+1)
    q.append((i, 0))
    v[i] = 1
    while q:
        busi, c = q.popleft()
        if c >= ans:
            break
        if busi in end:
            ans = min(c+1, ans)
        for j in r[busi]:
            if v[j] == 0:
                v[j] = 1
                q.append((j, c+1))
print(ans)
'''

'''
for _ in range(k):
    i, sh, sw, eh, ew = map(int, input().rstrip().split())
    g[i].append((sorted([sh, sw]), sorted([eh, ew])))
sx, sy, ex, ey = map(int, input().rstrip().split())

for i in g:
    print(*i)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        sh, sw = i[0]
        eh, ew = i[1]
        bsh, bsw = j[0]
        beh, bew = j[1]
'''



'''
from collections import deque
import sys
input = sys.stdin.readline


m, n = map(int, input().split())
k = int(input())
g = [set() for _ in range(k+1)]
for _ in range(k):
    i, sh, sw, eh, ew = map(int, input().rstrip().split())
    g[i].add((sh, sw))
    g[i].add((eh, ew))
    j = 1
    if sh == eh:
        if sw > ew:
            while ew+j < sw:
                print(sh, ew+j)
                g[i].add((sh, ew+j))
                j+=1
        elif ew > sw:
            while sw+j < ew:
                g[i].add((sh, sw+j))
                j+=1
    if sw == ew:
        if sh > eh:
            while eh+j < sh:
                g[i].add((eh+j, ew))
                j+=1
        elif eh > sh:
            while sh+j < eh:
                g[i].add((sh+j, sw))
                j+=1
sx, sy, ex, ey = map(int, input().rstrip().split())
q = deque()
for i in range(1, k+1):
    if (sx, sy) in g[i]:
        q.append((0, i, sx, sy, set())) # 버스 탄 횟수, 버스 번호, 좌표, 중복제거용
ans = int(10e9)
while q:
    bc, idx, h, w, jb = q.popleft()
    if h == ex and w == ey:
        ans = bc
        break
    for i in g[idx]:
        nh, nw = i
        q.append((bc+1, nh, nw, jb))


'''