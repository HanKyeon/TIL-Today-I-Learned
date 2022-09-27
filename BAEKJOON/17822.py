'''
원판 돌리기

반지름이 1~n인 원판이 크기가 작아지는 순으로 바닥에 놓여있고, 원판의 중심은 모두 같다. 원판의 반지름이 i면 그 원판을 i번째 원판이라고 한다. 각각의 원판네는 m개의 정수가 적혀있고, i번째 원판에 적힌 j번째 수의 위치는 i,j로 표현한다.

수의 위치는 다음을 만족한다.
(i, 1)은 (i, 2), (i, M)과 인접하다.
(i, M)은 (i, M-1), (i, 1)과 인접하다.
(i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)
(1, j)는 (2, j)와 인접하다.
(N, j)는 (N-1, j)와 인접하다.
(i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)

원판을 총 T번 회전 할 것임. 회전 방법은 정해져 있고, i번째 회전에 사용하는 변수는 xi di ki 이다.
1. 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
2. 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
2-1. 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
2-2. 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
원판을 T번 회전시킨 후 원판에 적힌 수의 합

입력
n, m, t 제시.
n개 줄에 우너판 적힌 수  제시.
i번째 줄의 j번째 수는 i번째 원판의 j번째 수.
T개 줄에 xi, di, ki 제시.

출력
원판을 T번 회전 시킨 후 적힌 수의 합.
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def bfs(h, w, val):
    global n
    q = deque([(h, w)])
    nq = [(h, w)]
    v = [[0]*m for _ in range(n)]
    v[h][w] = 1
    while q:
        h, w = q.popleft()
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if nw == m:
                nw = 0
            elif nw == -1:
                nw = m-1
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == val and not v[nh][nw]:
                v[nh][nw] = 1
                nq.append((nh, nw))
                q.append((nh, nw))
    if len(nq) == 1:
        return 0
    else:
        while nq:
            h, w = nq.pop()
            g[h][w] = 0
        return 1

def p1m1():
    global n
    di, num = set(), 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                continue
            num += 1
            di.add((i, j))
    if num == 0:
        return
    aver = sum(map(sum, g)) / num
    while di:
        h, w = di.pop()
        if g[h][w] > aver:
            g[h][w] -= 1
        elif g[h][w] < aver:
            g[h][w] += 1

def 돌려돌려돌림판(xi, di, ki):
    global n
    for i in range(xi-1, n, xi):
        j = ki
        if di:
            while j:
                g[i].append(g[i].popleft())
                j -= 1
        else:
            while j:
                g[i].appendleft(g[i].pop())
                j -= 1
    fla = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                continue
            fla += bfs(i, j, g[i][j])
    if not fla:
        p1m1()

n, m, t = map(int, input().rstrip().split())
g = [deque(list(map(int, input().rstrip().split()))) for _ in range(n)]
for _ in range(t): # xi의 배수인 원판을 di방향으로 ki칸 회전. di0 시계 di1 반시계
    xi, di, ki = map(int, input().rstrip().split())
    돌려돌려돌림판(xi, di, ki)
ans = sum(map(sum, g))
print(ans)


'''
# 짱 빠른 아재
import sys
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def go(a, x, d, k):
    if d == 0:
        a[x] = a[x][-k:] + a[x][:-k]
    else:
        a[x] = a[x][k:] + a[x][:k]


def check(a):
    n = len(a) - 1
    m = len(a[1])

    d = [[False]*m for _ in range(n+1)]

    ok = False # 같은 수 있으면 true, 아니면 false
    # d[i][j] = true (같은 수), false: (같은 수 아님)

    for i in range(1, n+1):
        for j in range(m):
            if a[i][j] == 0:
                continue
            if a[i][j] == a[i][(j+1)%m]:
                d[i][j] = d[i][(j+1)%m] = True
            if i+1 <= n and a[i][j] == a[i+1][j]:
                d[i][j] = d[i+1][j] = True
    for i in range(1, n+1):
        for j in range(m):
            if d[i][j]:
                ok = True
                a[i][j] = 0

    return ok

def adjust(a):
    n = len(a)-1
    m = len(a[1])
    total = 0 # sum
    cnt = 0

    for i in range(1, n+1):
        for j in range(m):
            if a[i][j] == 0:
                continue
            total += a[i][j]
            cnt += 1
    
    if cnt == 0:
        return
    
    for i in range(1, n+1):
        for j in range(m):
            if a[i][j] == 0:
                continue
            if total < a[i][j] * cnt:
                # total/cnt < a[i][j] (-1)
                a[i][j] -= 1
            elif total > a[i][j] * cnt:
                # total/cnt > a[i][j] (+1)
                a[i][j] += 1

n, m, t = map(int,input().split())
a = [None] + [list(map(int,input().split())) for _ in range(n)]

for _ in range(t):
    x, d, k = map(int,input().split())
    for y in range(x, n+1, x):
        go(a,y,d,k)

    ok = check(a)

    if ok == False:
        adjust(a)

ans = sum(sum(row) for row in a[1:])
print(ans)
'''









