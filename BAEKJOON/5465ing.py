'''
곰돌이

곰돌이가 비밀 꿀단지 발견. 꿀 먹으려는 순간 곰 발견해서 벌들에게 신호. 벌들의 공격을 피해 자신의 집으로 돌아가야 한다. 안전하게 집에 도착하기 위해 곰이 가장 늦게 떠나도 되는 시간 계산.
n*n 격자. 나무, 풀밭, 벌집, 곰집. 사방 이동만 가능. 나무나 벌집 이동 불가, 풀밭만 이동 가능. 1분 최대 s칸만큼 이동
벌집으로 이사 불가.
곰돌이가 꿀을 먹고 있다면 꿀을 먹을지 집으로 갈지 결정해야 한다. 꿀을 계속 먹으면 1분동안 무빙 불가. 가겠다고 결정하면 즉시 s칸 이동
1분동안 먹거나 움직인 뒤 1분이 완료되면, 벌들은 인접한 모든 칸으로 퍼져나간다. 동서남북, 풀밭 칸. 벌들이 있게 되면 영원히 벌들이 존재하게 된다. 마찬가지로 풀밭만.
벌이 신호를 보내는 순간 벌집이 있는 칸들에만 벌들이 있게 된다. 1분이 완료되면 인접한 칸과 모든 풀밭 칸을 차지. 2분이 완료되는 순간 bfs된다.
곰이 꿀을 먹는 시간은 정수 값. 벌들이 차지한 칸에 곰이 함께 있으면 안된다.
숲의 지도가 주어졌을 때, 곰돌이가 집에 도착하기 전에 벌들에게 잡히지 않으면서 꿀단지가 있는 위치에서 계속해서 꿀을 먹을 수 있는 가장 긴 시간을 계산.

입력
n, s 제시
n개 줄 지도 제시.
T나무 G풀밭 M곰 최초위치 D는 곰 집 H는 벌집
벌들은 곰돌이 집 통과 불가능.

출력
정수 하나 출력. 꿀을 계속해서 먹을 수 있는 가장 긴 시간
'''
'''
벌집에서 bfs해서 거리 잡아주기.
최대거리 추출 및 이분탐색으로 해당 값 이하로 이동 가능한 경로 탐색
'''
import sys
from collections import deque
input = sys.stdin.readline
wall, home = sys.maxsize, 1000001
mov = [(-1,0), (0,1), (1,0), (0,-1)]

def check(startTime):
    global ans, n, m, sh, sw, eh, ew
    iv = [[0]*n for _ in range(n)]
    q = deque([(sh, sw, startTime)])
    iv[sh][sw] = startTime
    while q:
        h, w, maxTime = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n:
                if g[nh][nw] == wall: continue
                if maxTime < g[nh][nw] and not iv[nh][nw]:
                    nextTime = v[nh][nw]+startTime
                    q.append((nh, nw, maxTime if maxTime > nextTime else nextTime))
                    iv[nh][nw] = maxTime if maxTime > nextTime else nextTime
                    # if startTime == 3:print(f"좌표는 ({nh}, {nw})일 때 {g[nh][nw]}, 지나온 최대 시간은 {maxTime}, 갈 곳의 시간은 {nextTime}")
    if startTime == 1:
        for i in iv: print(i)
    if iv[eh][ew]:
        if ans < startTime:
            ans = startTime
        return True
    return False

n, m = map(int, input().rstrip().split())
g, cs, v = [], deque(), [[-1]*n for _ in range(n)]
sh, sw, eh, ew = 0, 0, 0, 0
for i in range(n):
    s = list(input().rstrip())
    for j in range(n):
        if s[j] == 'T': s[j] = wall
        elif s[j] == 'G': s[j] = -1
        elif s[j] == 'M': s[j] = -1; sh, sw = i, j; v[i][j]=0
        elif s[j] == 'D': s[j] = home; eh, ew = i, j
        elif s[j] == 'H': cs.append((i, j)); s[j] = 0
    g.append(s)
# 곰 도착 시간 메모
q = deque([(sh, sw, 0)])
while q:
    h, w, cnt = q.popleft()
    ncnt = cnt//m
    for dh, dw in mov:
        nh, nw = h+dh, w+dw
        if 0<=nh<n and 0<=nw<n:
            if g[nh][nw] == home: v[nh][nw] = ncnt
            if g[nh][nw] < 0 and v[nh][nw] < 0:
                v[nh][nw] = ncnt
                q.append((nh, nw, cnt+1))
# 벌 도착 시간 메모
while cs:
    h, w = cs.popleft()
    for dh, dw in mov:
        nh, nw = h+dh, w+dw
        if 0<=nh<n and 0<=nw<n:
            if g[nh][nw] < 0:
                g[nh][nw] = g[h][w]+1
                cs.append((nh, nw))
            if g[nh][nw] == home: g[nh][nw] = g[h][w]+1
for i in range(n):
    for j in range(n):
        if g[i][j] == wall: g[i][j] = 0
for i in v: print(i)
print('===')
for i in g: print(i)
print('===')
# 이분 탐색
ans = 0
s, e = 0, g[sh][sw]-1
while s < e:
    mid = (s+e)//2
    if check(mid): s = mid+1; continue
    e = mid

print(ans if ans else -1)
