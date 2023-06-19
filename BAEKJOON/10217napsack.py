'''
KCM Travel

최대 M원까지 여행비 가능.
LA까지 M원 이하로 사용하면서 도착 할 수 있는 가장 빠른 길.

입력
공항수 n 2이상100이하 총지원비m 0이상 1만이하, 티켓정보 수 k 0이상1만이하 공백으로 구분 제시.
k개줄에 걸쳐 출발 공항u 도착공항v 1이상 n이하, 비용c 1이상m이하, 소요시간 d 1이상 1000이하 제시.
인천은 1번 LA는 N
'''

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
# sys.stdin = open("./BAEKJOON/input.txt")


for _ in range(int(input())):
    n, cost, m = map(int,input().split())
    dp = [[int(10e9)] * (n) for _ in range(cost+1)]
    graph = [[] for _ in range(n)]

    for i in range(m):
        u, v, c, d = map(int,input().split())
        graph[u-1].append((v-1, c, d))

    heap = [(0,0,0)] # 거리, 비용, 노드
    while(heap):
        Dnow, Cnow, Nnow = heappop(heap)
        if Dnow > dp[Cnow][Nnow]:
            continue
        for toNode,toCost,toDist in graph[Nnow]:
            d = Dnow + toDist
            c = Cnow + toCost
            if c <= cost and d < dp[c][toNode]:
                # 더 높은 cost를 투자할 때의 가중치도 맞춰준다.
                for i in range(c,cost+1):
                    if dp[i][toNode] > d:
                        dp[i][toNode] = d
                    else:
                        break
                heappush(heap,(d,c,toNode))
    # for i in dp:
    #     print(*i)
    print(dp[cost][n-1] if dp[cost][n-1] != int(10e9) else "Poor KCM")



'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij(sta, end):
    global dst
    dst = [int(10e9)] * (n+1)
    cst = [int(10e9)] * (n+1)
    dst[sta] = 0
    cst[sta] = 0
    heap = [(0, 0, sta)] # 소요시간, 비용, 노드
    while heap:
        timez, cost, nod = heappop(heap)
        if nod == end:
            return timez
        # if dst[nod] < timez:
        #     continue
        for i in g[nod]:
            ntime, nco, nnod = i
            if cost + nco > m:
                continue
            # if timez + ntime < dst[nnod]:
                # print(f"{nod}에서 {nnod}가는 길")
            dst[nnod] = min(dst[nnod], timez+ntime)
            heappush(heap, (timez+ntime, cost+nco, nnod))
    return dst[end]

for _ in range(int(input())):
    n, m, k = map(int, input().rstrip().split())
    g = [[] for _ in range(n+1)]
    ug = [[] for _ in range(n+1)]
    for _ in range(k):
        u, v, c, d = map(int, input().rstrip().split())
        g[u].append((d, c, v))
        ug[v].append((d, c, u))
    ans = dij(1, n)
    if ans == int(10e9):
        print('Poor KCM')
    else:
        print(ans)
'''


'''
1
6 149 8
1 2 60 20
2 3 30 70
1 3 100 80
1 3 20 180
3 4 20 100
3 5 150 20
5 6 50 40
4 6 30 50

240
'''




'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij(sta, end):
    global dst
    dst[sta] = 0
    heap = [(0, 0, sta)] # 소요시간, 비용, 노드
    while heap:
        timez, cost, nod = heappop(heap)
        if dst[nod] < timez:
            continue
        for i in g[nod]:
            ntime, nco, nnod = i
            if cost + nco > m:
                continue
            if timez + ntime < dst[nnod]:
                print(f"{nod}에서 {nnod}가는 길")
                dst[nnod] = timez+ntime
                heappush(heap, (timez+ntime, cost+nco, nnod))

for _ in range(int(input())):
    n, m, k = map(int, input().rstrip().split())
    g = [[] for _ in range(n+1)]
    dst = [int(10e9)] * (n+1)
    for _ in range(k):
        u, v, c, d = map(int, input().rstrip().split())
        g[u].append((d, c, v))
    print(g)
    dij(1, n)
    print(dst)
    if dst[n] == int(10e9):
        print('Poor KCM')
    else:
        print(dst[n])
'''

'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij(sta, end):
    global dst
    dst = [int(10e9)] * (n+1)
    dst[sta] = 0
    heap = [(0, 0, sta)] # 소요시간, 비용, 노드
    while heap:
        timez, cost, nod = heappop(heap)
        if dst[nod] < timez:
            continue
        for i in g[nod]:
            ntime, nco, nnod = i
            if cost + nco > m:
                continue
            if timez + ntime < dst[nnod]:
                # print(f"{nod}에서 {nnod}가는 길")
                dst[nnod] = timez+ntime
                heappush(heap, (timez+ntime, cost+nco, nnod))
    return dst[end]
def dij2(sta, end):
    global dst
    dst = [int(10e9)] * (n+1)
    dst[sta] = 0
    heap = [(0, 0, sta)] # 소요시간, 비용, 노드
    while heap:
        timez, cost, nod = heappop(heap)
        if dst[nod] < timez:
            continue
        for i in ug[nod]:
            ntime, nco, nnod = i
            if cost + nco > m:
                continue
            if timez + ntime < dst[nnod]:
                # print(f"{nod}에서 {nnod}가는 길")
                dst[nnod] = timez+ntime
                heappush(heap, (timez+ntime, cost+nco, nnod))
    return dst[end]

for _ in range(int(input())):
    n, m, k = map(int, input().rstrip().split())
    g = [[] for _ in range(n+1)]
    ug = [[] for _ in range(n+1)]
    for _ in range(k):
        u, v, c, d = map(int, input().rstrip().split())
        g[u].append((d, c, v))
        ug[v].append((d, c, u))
    ans = min(dij(1, n), dij2(n, 1))
    if ans == int(10e9):
        print('Poor KCM')
    else:
        print(ans)
'''





