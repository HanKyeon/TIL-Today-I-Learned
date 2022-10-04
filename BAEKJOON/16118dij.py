'''
달빛 여우

달빛 여우가 보름달 받으면 구미호로 변신. 달빛 늑대도 있음.
1번부터 n번까지 n개의 그루터기, m개의 오솔길. 두 그루터기 사이 유일한 오솔길.
여우와 늑대는 1번 그루터기 존재.
달빛 여우와 달빛 늑대가 경쟁해서 달려간다.
달빛 늑대는 여우보다 빠르게 달리지만 체력 부족.
1. 달빛 늑대는 출발 할 때 오솔길 하나를 달빛 여우의 두배 속도로 갈려가고, 그 뒤로는 오솔길 하나를 달빛 여우의 절반의 속도로 걸어가며 체력 회복.
2. 이후 다시 달빛 여우 두배 속도로 달려간다.
3. 달빛 여우는 늘 일정한 속도로 달려간다.
-> 둘의 이동 경로가 서로 다를 수 있다.

달빛 여우가 달빛 늑대보다 먼저 도착 할 수 있는 그루터기가 몇개나 있는가?

입력
n, m 제시.
m개 줄 a, b, c 제시. a와 b 사이에 c 오솔길

출력
달빛 여우가 달빛 늑대보다 먼저 도착 할 수 있는 나무 그루터기 갯수 출력
'''
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def fox():
    global n
    dst = [int(10e9)]*(n+1)
    dst[1] = 0
    heap = [(0, 1)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        for co, nnod in g[nod]:
            if dst[nnod] > cost+co:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    return dst

def wolf1():
    global n
    dst = [[int(10e9), int(10e9)] for _ in range(n+1)]
    dst[1] = [0, 0]
    heap = [(0, 1, 1)]
    while heap:
        cost, nod, fla = heappop(heap)
        if dst[nod][fla] < cost:
            continue
        for co, nnod in g[nod]:
            if fla:
                costco = cost + co//2
            else:
                costco = cost + co*2
            if dst[nnod][(fla+1)%2] > costco:
                dst[nnod][(fla+1)%2] = costco
                heappush(heap, (cost+co, nnod, (fla+1)%2))
    dst = list(map(min, dst))
    return dst

def wolf0():
    global n
    dst = [[int(10e9), int(10e9)] for _ in range(n+1)]
    dst[1] = [0, 0]
    heap = [(0, 1, 0)]
    while heap:
        cost, nod, fla = heappop(heap)
        if dst[nod][fla] < cost:
            continue
        for co, nnod in g[nod]:
            if fla:
                costco = cost + co//2
            else:
                costco = cost + co*2
            if dst[nnod][(fla+1)%2] > costco:
                dst[nnod][(fla+1)%2] = costco
                heappush(heap, (cost+co, nnod, (fla+1)%2))
    dst = list(map(min, dst))
    return dst

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c*2, b))
    g[b].append((c*2, a))

# w0 = wolf0()
# w1 = wolf1()
w = list(map(min, zip(wolf0(), wolf1())))
f = fox()
ans = 0
for i in range(1, n+1):
    if w[i] <= f[i]:
        continue
    ans += 1
print(ans)
'''



from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def fox():
    dst = [int(10e9)]*(n+1)
    dst[1] = 0
    heap = []
    heappush(heap, (0, 1))
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        for co, nnod in g[nod]:
            costco = cost + co
            if costco < dst[nnod]:
                dst[nnod] = costco
                heappush(heap, (costco, nnod))
    return dst

def wolf():
    dst = [[int(10e9)]*2 for _ in range(n+1)]
    dst[1][1] = 0
    heap = [(0, 1, 0)]
    while heap:
        cost, nod, fla = heappop(heap)
        if fla and dst[nod][0] < cost:
            continue
        elif not fla and dst[nod][1] < cost:
            continue
        for co, nnod in g[nod]:
            if fla:
                costco = cost + (co * 2)
                if costco < dst[nnod][fla]:
                    dst[nnod][fla] = costco
                    heappush(heap, (costco, nnod, fla-1))
            else:
                costco = cost + (co // 2)
                if costco < dst[nnod][fla]:
                    dst[nnod][fla] = costco
                    heappush(heap, (costco, nnod, fla+1))
    dst = map(min, dst)
    return dst

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((c*2, b))
    g[b].append((c*2, a))

ans = 0
for f, w in zip(fox(), wolf()):
    if f < w:
        ans += 1
print(ans)


'''
# 빠른 코드

"""
빠_늑대: x//2 -> x
여우 : x -> x*2
느_늑대: x*2 -> x*4
"""

import heapq
import sys
input = sys.stdin.readline

def dijkstra(G):
    l = len(G)-1
    dist = [float('inf')]*(l+1)
    dist[1] = 0
    H = [(0, 1)]
    
    while H:
        v, now = heapq.heappop(H)
        if dist[now] != v: continue
        
        for gv, gn in G[now]:
            if dist[gn]>gv+v:
                dist[gn] = gv+v
                heapq.heappush(H, (gv+v, gn))
    return dist            
    
    
N, M = map(int, input().split())
W = [[] for _ in range(2*N+1)]
F = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, v = map(int,input().split())
    F[a].append((2*v, b))
    F[b].append((2*v, a))
    W[a].append((v, N+b))
    W[b].append((v, N+a))
    W[N+a].append((4*v, b))
    W[N+b].append((4*v, a))
    

dis_f = dijkstra(F)
dis_w = dijkstra(W)

res= 0 
for i in range(2, N+1):
    if dis_f[i] < min(dis_w[i], dis_w[i+N]):
        res += 1
print(res)
'''



'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def fox():
    global n
    dst = [int(10e9)]*(n+1)
    dst[1] = 0
    heap = [(0, 1)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        for co, nnod in g[nod]:
            if dst[nnod] > cost+co:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    return dst

def wolf1():
    global n
    dst = [[int(10e9), int(10e9)] for _ in range(n+1)]
    dst[1] = [0, 0]
    heap = [(0, 1, 1)]
    while heap:
        cost, nod, fla = heappop(heap)
        if dst[nod][fla] < cost:
            continue
        for co, nnod in g[nod]:
            if fla:
                costco = cost + co//2
            else:
                costco = cost + co*2
            if dst[nnod][(fla+1)%2] > costco:
                dst[nnod][(fla+1)%2] = costco
                heappush(heap, (costco, nnod, (fla+1)%2))
    for i in zip(*dst):
        print(i)
    dst = list(map(min, dst))
    return dst
def wolf0():
    global n
    dst = [[int(10e9), int(10e9)] for _ in range(n+1)]
    dst[1] = [0, 0]
    heap = [(0, 1, 0)]
    while heap:
        cost, nod, fla = heappop(heap)
        if dst[nod][fla] < cost:
            continue
        for co, nnod in g[nod]:
            if fla:
                costco = cost + co//2
            else:
                costco = cost + co*2
            if dst[nnod][(fla+1)%2] > costco:
                dst[nnod][(fla+1)%2] = costco
                heappush(heap, (costco, nnod, (fla+1)%2))
    for i in zip(*dst):
        print(i)
    dst = list(map(min, dst))
    return dst

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))

# w0 = wolf0()
# w1 = wolf1()
# w = list(map(min, zip(wolf0(), wolf1())))
w = wolf1()
f = fox()
w = list(map(min, zip(wolf1(), wolf0())))
print(w)
print(f)
ans = 0
for i in range(1, n+1):
    if w[i] <= f[i]:
        continue
    ans += 1

print(ans)
'''








