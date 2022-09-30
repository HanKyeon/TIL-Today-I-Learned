'''
상어 중학교

n*n 격자
격자에블록이 다 들어있고, 검은색 무지개 일반 블록 있다.
일반 블록은 m가지 색깔 존재. 1~m으로 표현. 검은색-1 무지개0
상하좌우 인접칸
블록 그룹은 연결된 블록 집합.
최소 1일반 블록, 그룹 내 일반 블록 색은 동일. not black, ok rainbow
그룹에 속한 블록의 갯수는 2보다 크거나 같아야하며, 임의의 한 블록에서 그룹에 속한 인접 ㅋ칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다.
블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 좌상단의 블록이다.

오토플레이 할 것이다. 아래 과정이 반복된다.
1. 크기가 가장 큰 블록 그룹 탐색. 같은 크기가 있다면 무지개 블록의 수가 가장 많은 그룹 선택. 여러개라면 기준 블록의 행이 가장 큰 것, 그것도 여러개면 열이 가장 큰 것.
2. 1에서 찾은 블록 그룹의 모든 블록 제거. 블록 수를 b라고 할 때 b**2 점 횟득.
3. 격자에 중력 작용.
4. 격자가 90도 반시계 방향으로 회전.
5. 다시 격자에 중력 작용.

격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다. 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속된다.

입력
한 변의 크기 n, 색상 갯수 m
그래프 제시.

출력
점수합 출력
'''
from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def no1():
    global n
    def find(ph, pw, val):
        global n
        q = deque([(ph, pw)])
        v[ph][pw] = 1
        nq = [] # h, w 가 무지개 블록일 때는 걸러서 들어온다.
        ret = [(ph, pw)]
        while q:
            h, w = q.popleft()
            for i in range(4):
                nh, nw = h+dh[i], w+dw[i]
                if 0<=nh<n and 0<=nw<n and g[nh][nw] == val and not v[nh][nw]:
                    v[nh][nw] = 1
                    q.append((nh, nw))
                    ret.append((nh, nw))
                elif 0<=nh<n and 0<=nw<n and g[nh][nw] == 0 and not v[nh][nw]:
                    v[nh][nw] = 1
                    q.append((nh, nw))
                    ret.append((nh, nw))
                    nq.append((nh, nw))
        rbb = len(nq)
        while nq:
            h, w = nq.pop()
            v[h][w] = 0
        return -len(ret), -rbb, ret
    
    v = [[0]*n for _ in range(n)]
    heap = []
    for i in range(n):
        for j in range(n):
            if g[i][j] <= 0:
                continue
            rett = find(i, j, g[i][j])
            heappush(heap, (rett[0], rett[1], -i, -j, rett[2]))
    if heap:
        ret = heappop(heap)
        return ret[-1]
    else:
        return []

def gravity():
    global n, g
    for i in range(n):
        sta, now = n-1, n-2
        while 0<= now < n and 0<=sta<n:
            if g[sta][i] == -2 and g[now][i] >= 0:
                g[sta][i], g[now][i] = g[now][i], g[sta][i]
                sta -= 1
                continue
            if g[sta][i] != -2:
                sta -= 1
                now = sta-1
                continue
            if g[now][i] == -2: 
                now-=1
                continue
            if g[now][i] == -1:
                sta = now-1
                now -= 1
                continue

def turn90():
    global n, g
    ng = []
    for i in g:
        ng.append(i[:])
    for i in range(n):
        for j in range(n):
            g[i][j] = ng[j][n-1-i]

n, m = map(int, input().rstrip().split())
clinfo = [[] for _ in range(m+1)]
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
ans = 0
suba = no1()
while len(suba) >= 2:
    ans += len(suba)**2
    for i in suba:
        h, w = i
        g[h][w] = -2
    # 중력
    gravity()
    # 회전
    turn90()
    # 중력
    gravity()
    suba = no1()

print(ans)
















