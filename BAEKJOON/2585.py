'''
경비행기

경비행기 독수리호가 출발지 S에서 목적지 T로 이동.
연료통 크기 중요. 큰건 급유 횟수 적지만 무게때매 느려짐 작으면 빨라지지만 급유 많이 함. 급유 횟수 k이하일 때 연료통 최소 용량.
최소 연료통의 크기를 구해라.
1. 모든 비행기는 직선으로 날아가고 거리는 km, 단위는 리터. 1리터당 10km 주행, 연료 주입 리터 단위.
2. 평면상 거리로 본다.
3. S는 0,0 T는 1만,1만 고정
4. 비행장 수는 3개이상 1000이하. 0부터 1만 사이, 급유 횟수는 0이상 1000이하

입력
n, k 제시.
n개 줄 x, y로 급유지 제시.

출력
S에서 T까지 k번 이하로 중간급유하여 갈 수 있는 항로에서의 최소 연료통 용량에 해당하는 정수 출력.
'''
import sys
from collections import deque
input = sys.stdin.readline

def setDst(i,j):
    l = ((g[i][0] - g[j][0])**2 + (g[i][1] - g[j][1])**2)**(1/2)
    l = int((l // 10) + 1 if l % 10 else (l // 10))
    dst[i][j], dst[j][i] = l, l

def check(maxCnt):
    v = set([0])
    q = deque([(0,0)])
    while q:
        nod, cnt = q.popleft()
        if dst[nod][n+1] <= maxCnt:
            return True
        if cnt >= k: continue
        for nnod in range(n+2):
            if nnod not in v and dst[nod][nnod] <= maxCnt:
                v.add(nnod)
                q.append((nnod,cnt+1))
    return False

n, k = map(int, input().rstrip().split())
g = [(0,0)] + [tuple(map(int,input().rstrip().split())) for _ in range(n)] + [(10000,10000)]
dst = [[0] * (n+2) for _ in range(n+2)]
for i in range(n+2):
    for j in range(n+2):
        setDst(i,j)

sta, end = 0, dst[0][-1]
ans = 0
while sta <= end:
    mid = (sta + end) // 2
    if check(mid):
        ans = mid
        end = mid - 1
    else:
        sta = mid + 1
print(ans)

'''
# 빠른 코드

from collections import deque
import sys
import math
input = sys.stdin.readline

# 기준은 연료통으로


def calc(c1, c2):
    return (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2


def bfs(cur, cnt):
    q = deque([(cur, cnt)])  # 처음부터 시작, k = 0
    visited = [False] * (n + 2)
    visited[0] = True

    while q:
        idx, cnt = q.popleft()
        if idx == n + 1:
            return True
        if cnt > k:
            continue
        for i in range(1, n + 2):
            if cnt <= k and not visited[i]:
                if dist[idx][i] <= cost:
                    visited[i] = True
                    q.append((i, cnt + 1))

    return False


n, k = map(int, input().split())

graph = [[0, 0]] + [list(map(int, input().split()))
                    for _ in range(n)] + [[10000, 10000]]
ans = 0

dist = [[0] * (n + 2) for _ in range(n + 2)]

for i in range(n + 1):
    for j in range(i, n + 2):
        if i == j:
            dist[i][j] = float('inf')
        else:
            dist[i][j] = dist[j][i] = calc(graph[i], graph[j])

# 최소, 최대 연료통
pl, pr = 1, 1415

while pl <= pr:
    mid = (pl + pr) // 2
    cost = mid ** 2 * 100
    if bfs(0, 0):
        pr = mid - 1
        ans = mid
    else:
        pl = mid + 1

print(ans)
'''

'''
# 시간 초과

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def checkNode(i, j):
    x1, y1 = nodz[i]
    x2, y2 = nodz[j]
    ret = (abs(x1-x2)**2+abs(y1-y2)**2)**0.5
    g[i][j], g[j][i] = ret, ret

n, k = map(int, input().rstrip().split())
nodz = []
for _ in range(n):
    x, y = map(int, input().rstrip().split())
    nodz.append((x, y))
n+=2
nodz = [(0,0)] + nodz + [(10000, 10000)]
g = [[0]*n for _ in range(n)]
for i in range(n-1):
    for j in range(i+1, n):
        checkNode(i, j)
q = deque([(0, k)])
ans = (g[0][-1]//10+1) if g[0][-1]%10 else g[0][-1]//10
for i in range(1, k+1):
    for combi in combinations(range(1, n-1), i):
        nod, ret = 0, 0
        for nnod in combi:
            v = (g[nod][nnod]//10+1) if g[nod][nnod]%10 else g[nod][nnod]
            if ret < v:
                ret = v
            nod = nnod
        v = (g[nod][-1]//10+1) if g[nod][-1]%10 else g[nod][-1]
        if ret < v:
            ret = v
        if ans > ret:
            ans = ret
print(int(ans))

'''


