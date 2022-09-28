'''
스타트 택시

손님을 도착지로 데려다 줄 때마다 연료가 충전, 연료 바닥나면 그 날 업무 끝
M명의 승객 태울 것. n*n 격자.
승객은 좌표 위의 어따 올려둠. 최단거리 이동.
여러 승객 탐승 없음. 한 승객을 태워 목적지로 이동시키는 일을 M번 반복해야 한다.
최단 거리의 승객을 선택, 연료는 한 칸마다 1 소모, 승객을 무사히 이동 시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두배가 충전. 도중 연료가 바닥나면 이동 실패, 그 날 업무 종료.이동과 동시에 연료가 바닥나는 경우 실패 아님.
모든 승객을 잘 데려다줄 수 있는지, 그럴 수 있다면 최종적으로 남는 연료의 양 출력.

입력
n, m 초기연료 제시. 연료는 무제한 충전 가능.
지도 제시. 1은 벽
백준이 운전 시작하는 칸의 행 번호와 열 번호 제시.
M개 줄에 각 승객의 출발지의 행과 열 번호, 목적지의 행과 열 번호 제시.
모든 출발지와 목적지는 빈 칸이고, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.

출력
다 이동 시킨 뒤 남은 연료 양 출력. 이동 중 연료 바닥나거나 모든 손님 이동 안되면 -1 출력
'''
from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def find(ptxh, ptxw, fuel):
    global n, k
    if g[ptxh][ptxw] >= 2:
        idx = g[ptxh][ptxw]
        g[ptxh][ptxw] = 0
        return idx, ptxh, ptxw
    v = [[0]*n for _ in range(n)]
    v[ptxh][ptxw] = 1
    q = deque([(ptxh, ptxw, fuel, 0)])
    ret = []
    ndep = 0
    while q:
        h, w, fuel, dep = q.popleft()
        if ndep != dep:
            if ret:
                h, w, idx, fuel = heappop(ret)
                k = fuel
                g[h][w] = 0
                return idx, h, w
            ndep = dep
        if fuel < 0:
            return -500, 30, 30
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<n and not v[nh][nw] and g[nh][nw] != 1:
                if g[nh][nw] == 0:
                    v[nh][nw] = 1
                    q.append((nh, nw, fuel-1, dep+1))
                elif g[nh][nw] >= 2:
                    v[nh][nw] = 1
                    q.append((nh, nw, fuel-1, dep+1))
                    heappush(ret, (nh, nw, g[nh][nw], fuel-1))
    return 500, 30, 30

def lego(sh, sw, idx, fuel):
    global n, k
    if gst.get(idx, 0):
        th, tw = gst[idx]
    else:
        return 500, 500
    v = [[0]*n for _ in range(n)]
    v[sh][sw] = 1
    q = deque([(sh, sw, fuel, 0)])
    while q:
        h, w, fuel, dep = q.popleft()
        if fuel < 0:
            return -500, -500
        if h == th and w == tw:
            k = fuel + dep*2
            return h, w
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<n and not v[nh][nw] and g[nh][nw] != 1:
                v[nh][nw] = 1
                q.append((nh, nw, fuel-1, dep+1))
    return 500, 500


n, m, k = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
# ansb = sum(map(sum, g))
txh, txw = map(int, input().rstrip().split())
txh-=1
txw-=1
gst = {}
for i in range(2, m+2):
    h, w, th, tw = map(int, input().rstrip().split())
    g[h-1][w-1] = i
    gst[i] = (th-1, tw-1)

# for i in g:
#     print(i)
# print('===')

for i in range(m):
    idx, h, w = find(txh, txw, k)
    # print(idx, h, w, k)
    # for i in g:
    #     print(i)
    # print('===')
    if idx == 500 or idx == -500:
        k = -1
        break
    txh, txw = h, w
    h, w = lego(txh, txw, idx, k)
    txh, txw = h, w
    if txh == -500 or txh == 500:
        k = -1
        break

# ans = sum(map(sum, g))
# if ans != ansb:
#     k = -1
# if txh > 100:
#     k = -1
print(k)

'''
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 5
0 0 0 0 6 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
'''




'''
def find(txh, txw, fuel):
    global n, k
    if g[txh][txw] > 2:
        g[txh][txw] = 0
        return txh, txw, g[txh][txw]
    v = [[0]*n for _ in range(n)]
    q = deque([(txh, txw, fuel, 0), ('확', '인')])
    nq = []
    v[txh][txw] = 1
    while q:
        info = q.popleft()
        if len(info) == 2:
            if not nq:
                q.append(info)
                continue
            elif nq:
                idx, h, w, fuel, dep = heappop(nq)
                g[h][w] = 0
                k = fuel + dep*2
                return h, w, idx
        else:
            h, w, fuel, dep = info
            if fuel-1 < 0:
                return (-1, -1, -1)
            for i in range(4):
                nh, nw = h+dh[i], w+dw[i]
                if 0<=nh<n and 0<=nw<n and g[nh][nw] == 0 and not v[nh][nw]:
                    q.append((nh, nw, fuel-1, dep+1))
                    v[nh][nw] = 1
                if 0<=nh<n and 0<=nw<n and g[nh][nw] >= 2 and not v[nh][nw]:
                    heappush(nq, (g[nh][nw], nh, nw, fuel-1, dep+1))
    return (30, 30, 30)
'''