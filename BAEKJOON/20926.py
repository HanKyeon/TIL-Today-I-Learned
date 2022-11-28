'''
얼음 미로

테라는 얼음 미로에 갇혔다. 4가지 오브젝트.
1. 테라 : 주인공. 상하좌우 4방이동 가능. 1개만 존재, 최초 위치한 곳의 미끌 시간은 0
2. 바위 : 통과x, 미끄러지다 부딪히면 앞에서 정지.
3. 구멍 : 빠지면 안됨
4. 출구 : 방문 즉시 탈출. 단 1개의 출구만 존재.

빙판 위에서 미끄러지는데 걸리는 시간을 미끌 시간이라 한다. 빙판마다 미끌 시간이 다를 수 있다.
테라가 어느 한 쪽 방향으로 이동 할 때, 테라가 미끄러지는 동안 위치한 빙판의 미끌 시간을 더하면 이동 시간을 구할 수 있다.
이동 시간과 관련한 두가지 규칙
1. 테라가 어느 한쪽 방향으로 이동을 시작 할 때, 시작 빙판의 미끌 시간은 포함x
2. 테라가 출구로 들어갈 때 출구의 미끌 시간은 포함하지 않는다.

입력
가로 크기 m, 세로크기 n 제시.
n개 줄 정보 제시.
T는 테라 R은 바위 구멍은H 출구는 E
미끌 시간은 0이상 9이하
미로 밖으로 빠져나갈 수 없다.

출력
탈출 가능 시 최단 탈출 시간
불가능 시 -1
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def move(h:int, w:int, di:int):
    global n, m, eh, ew
    dh, dw = mov[di]
    nh, nw = h+dh, w+dw
    ret= 0
    if nh < 0 or nh >= n or nw < 0 or nw >= m:
        return False
    while 0 <= g[nh][nw] < 10:
        ret += g[nh][nw]
        nh, nw = nh+dh, nw+dw
        if nh < 0 or nh >= n or nw < 0 or nw >= m:
            return False
    if h == nh and w == nw:
        return False
    if g[nh][nw] == -1:
        return False
    elif g[nh][nw] == 11:
        return (ret, True)
    elif g[nh][nw] == 10:
        nh, nw = nh-dh, nw-dw
        return (nh, nw, ret)

def dij()->int:
    global n, m, sh, sw, eh, ew
    dst[sh][sw] = 0
    heap = [(0, sh, sw)]
    while heap:
        cost, h, w = heappop(heap)
        if dst[h][w] < cost:
            continue
        if h == eh and w == ew:
            return cost
        for i in range(4):
            a = move(h, w, i)
            if a:
                if len(a) == 3:
                    nh, nw, co = a
                    if dst[nh][nw] > cost+co:
                        dst[nh][nw] = cost+co
                        heappush(heap, (cost+co, nh, nw))
                elif len(a) == 2:
                    co, fla = a
                    heappush(heap, (cost+co, eh, ew))
            else:
                continue
    return -1


m, n = map(int, input().rstrip().split())
g = []
for i in range(n):
    s = list(input().rstrip())
    for j in range(m):
        if s[j] == 'T':
            sh, sw = i, j
            s[j] = '0'
        elif s[j] == "R":
            s[j] = '10'
        elif s[j] == "H":
            s[j] = "-1"
        elif s[j] == "E":
            eh, ew = i, j
            s[j] = '11'
    s = list(map(int, s))
    g.append(s)
dst = [[int(10e9)]*(m) for _ in range(n)]

print(dij())




