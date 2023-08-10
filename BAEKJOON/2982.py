'''
국왕의 방문

차량 통제할 것
여러개 교차로를 연결하는 양방향 도로. 도로를 이동하는데 걸리는 시간 안다.
고돌라가 10분에 진입하고 5분이 걸리면 10 11 12 13 14 까지 진입 금지. 9분 이전 10분 이후 도로 진입 가능.
배달하는데 걸리는 시간 최솟값을 구하시오.

입력
n, m 제시 1번부터 n번
s, e, cha, cnt 제시. a는 배달 시작 교차로, b는 마치는 교차로. k는 출발 시간과 상근이 출발 시간 차이, g는 방문 갯수.
g개의 정수 제시. 고돌라가 방문하는 교차로. 인접하는 교차로이며 도로는 항상 존재한다.
m개 줄에는 도로 정보 a, nl, cnt 제시. u에서 v까지 l만큼 걸린다.

출력
배달 마치는데 필요한 가장 빠른 시간 출력
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

INF = sys.maxsize
n, m = map(int, input().rstrip().split())
s, e, cha, cnt = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))
times = [0 for _ in range(cnt-1)]
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
    if a in nl and b in nl and abs(nl.index(a)-nl.index(b)) == 1:
        if nl.index(a) > nl.index(b):
            times[nl.index(b)] = c
        else:
            times[nl.index(a)] = c
for i in range(1, cnt-1):
    times[i] += times[i-1]
def check(val):
    for i in range(cnt-1):
        if val < times[i]:
            return (nl[i], nl[i+1], times[i])
    return (-1, -1, -1)
def dij(start, cha):
    dst = [INF]*(n+1)
    dst[start] = cha
    heap = [(cha, start)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost: continue
        a, b, t = check(cost)
        for co, nnod in g[nod]:
            delay = 0
            if (a == nod and b == nnod) or (a == nnod and b == nod):
                delay = t - cost
            if dst[nnod] > delay + cost + co:
                dst[nnod] = delay + cost + co
                heappush(heap, [dst[nnod], nnod])
    return dst[e] - cha
print(dij(s, cha))
'''
# 빠른 코드
import sys
import heapq

read = sys.stdin.readline


def dijkstra(s, e):
    res = [float('inf') for _ in range(N + 1)]
    res[s] = 0

    q = []
    heapq.heappush(q, [0, s])

    while q:
        curr_t, curr_n = heapq.heappop(q)

        if curr_n == e: return res[e]

        if res[curr_n] < curr_t :
            continue

        for cn, cw in grp[curr_n].items():
            time = cw + curr_t
            if (curr_n, cn) in godul_move: #현재 노드에서 자식노드로 가는 길을 고둘라가 지나는지
                ge = godul_move[(curr_n, cn)][1]  #마지막으로 지나는 시간
                gs = godul_move[(curr_n, cn)][0]  #처음진입시간
                if gs <= curr_t + K <= ge:  #만약 고둘라가 도로를 지나갈때 들어가려한다면 
                    res[curr_n] = ge + 1 - K
                    heapq.heappush(q,[ge + 1 - K,curr_n])
                    continue

            if res[cn] > time:
                res[cn] = time
                heapq.heappush(q, [time, cn])

    return res[e]

if __name__ == '__main__':
    N, M = map(int, read().split())
    A, B, K, G = map(int, read().split())
    godul = list(map(int, read().split()))

    grp = [dict() for _ in range(N + 1)]

    for _ in range(M):
        U, V, L = map(int, read().split())
        grp[U][V] = L
        grp[V][U] = L

    godul_move = dict()  #고둘라의 각 동선마다 시간대 체크 ex( key (5,3) : value[4,10]   -> 5에서 3까지가는 도로를 4분부터 10분까지 점령
    time_sum = 0
    for i in range(len(godul) - 1):
        s, e = godul[i], godul[i + 1]
        godul_move[(s, e)] = [time_sum, time_sum + grp[e][s] - 1] #5분걸리는 도로를 0분부터 시작하면 0,1,2,3,4 이므로 -1을 해줌.
        godul_move[(e, s)] = [time_sum, time_sum + grp[e][s] - 1] #도로는 양방향이므로
        time_sum += grp[e][s]
    print(dijkstra(A, B))
'''
'''
# 틀린 코드

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def check(val):
    global cnt
    for i in range(1, cnt-1):
        if limits[i-1][2] <= val < limits[i][2]:
            return limits[i]
    return 0, 0, 0

def lego():
    global s, e, cha, cnt
    dst = [int(10e9)] * (n+1)
    dst[s] = cha
    heap = [(cha, s)] # 시간 / 교차로
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        if nod == e:
            return cost - cha
        a, b, num = check(cost)
        for nnod in range(1, n+1):
            co = g[nod][nnod]
            if not co:
                continue
            delay = (num-cost) if (a == nod and b == nnod) or (a == nnod and b == nod) else 0
            costco = delay + cost + co
            if dst[nnod] > costco:
                dst[nnod] = costco
                heappush(heap, (costco, nnod))

n, m = map(int, input().rstrip().split()) # n, m 제시
s, e, cha, cnt = map(int, input().rstrip().split()) # 시작 도착 출발 시간 차이 방문 갯수
nl = list(map(int, input().rstrip().split())) # cnt개의 정수
g = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a][b], g[b][a] = c, c
limits = []
for i in range(cnt-1):
    limits.append((nl[i], nl[i+1], g[nl[i]][nl[i+1]] + (0 if not limits else limits[-1][2])))
print(lego())
'''
