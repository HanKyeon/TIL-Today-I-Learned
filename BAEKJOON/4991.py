'''
로봇 청소기

유저가 직접 경로를 설정 할 수 있다. 깨끗한 칸과 더러운 칸. 더러운칸을 깨끗이.
가구 존재. 가구로 이동 금지.
인접 칸 이동. 재방문 가능. 더러운 칸을 모두 깨끗한 칸으로 만드는데 필요한 이동 횟수의 최솟값을 구하는 프로그램 작성.

입력
여러개 테케로 존재하며 0 0 입력되면 종료.
가로 w, 세로 h 제시. 1이상 20이하
h개에 방의 정보 제시.
. 깨끗
* 더버
x 가구
o 청소기 시작 위치

출력
이동 횟수의 최솟값을 한 줄에 하나씩 출력. 방문 할 수 없는 더러운 칸이 존재하는 경우에는 -1 출력.
'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(-1,0),(0,1),(1,0),(0,-1)]

def dstset(h, w, idx):
    global n, m
    v = [[0]*m for _ in range(n)]
    q = deque([(h, w)])
    v[h][w] = 1
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == '.' and not v[nh][nw]:
                v[nh][nw] = v[h][w]+1
                q.append((nh, nw))
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] == '*' and not v[nh][nw]:
                v[nh][nw] = v[h][w]+1
                dst[idx][di[(nh, nw)]] = v[h][w]
                dst[di[(nh, nw)]][idx] = v[h][w]
                q.append((nh, nw))

def dfs(nidx, val, cnt):
    global nodc, ans
    if val >= int(10e9):
        return
    if val >= ans:
        return
    if cnt == nodc:
        ans = min(ans, val)
        return
    for i in range(nodc):
        if v[i]:
            continue
        cost = dst[nidx][i]
        if cost == int(10e9):
            continue
        v[i] = 1
        dfs(i, val+cost, cnt+1)
        v[i] = 0

while True:
    m, n = map(int, input().rstrip().split())
    if not m and not n:
        break
    g = [list(input().rstrip()) for _ in range(n)]
    nodes = []
    rh, rw = 0, 0
    cnt = 0
    di = {}
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'o':
                rh, rw = i, j
                g[i][j] = '.'
            elif g[i][j] == '*':
                cnt+=1
                nodes.append((i, j))
                di[(i, j)] = cnt
    nodes = [(rh, rw)] + nodes
    nodc = len(nodes)
    dst = [[int(10e9)]*nodc for _ in range(nodc)]
    for i in range(nodc):
        h, w = nodes[i]
        dstset(h, w, i)
    ans = int(10e9)
    v = [0]*nodc
    v[0] = 1
    dfs(0, 0, 1)
    if ans == int(10e9):
        ans = -1
    print(ans)


