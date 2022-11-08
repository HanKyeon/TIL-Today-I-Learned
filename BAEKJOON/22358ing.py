'''
스키장

스키장에는 중간지점 n개 존재. 고도가 감소하는 순서대로 1부터 n까지. 1이 젤 높다.
s번에 있는 당신. 스키 탄 이후 끝나면 t번에서 모이기로 함.
m개 코스 존재. ai에서 bi로 이어지며 코스 진입 시 ti 시간동안 스키탄다.
코스는 항상 고도가 감소하는 방향으로. ai<bi 항상 만족.
코스에는 스키 리프트. 반대방향. 고도가 증가하는 방향으로 이어져 있다.
스키 리프트는 최대 k번 탑승 가능.
스키 코스랑 리프트만 써서 T번 지점 갈 것이며 스키 타는 시간 최대화 할 것.
리프트 타는 시간은 스키 타는 시간에 포함x

입력
5개 정수 n, m, k, s, t 제시.
노드 수 n 간선 수 m 리프트 최대 탑승 횟수 k, 시작 노드 s, 목표 노드 t
m개 줄 코스 정보 제시.

출력
최대 몇 시간 동안 스키를 탈 수 있는가?
어떤 선택을 해도 T번 지점에 이동 못하면 -1 출력.
'''
import sys
from collections import deque
from heapq import heappop, heappush
from math import inf
input = sys.stdin.readline

n, m, k, sta, end = map(int, input().rstrip().split())
g = [[inf]*(n+1) for _ in range(n+1)]
godown = [[] for _ in range(n+1)]
lift = [set() for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    godown[a].append((c, a))
    lift[b].add(a)

v = [[-1]*(k+1) for _ in range(n+1)]


print(dij())

# print(bfs())
# print(godown)
# print(lift)
# print(v)


'''
# bfs, dfs, dij 시간 초과.
v = [[-1]*(k+1) for _ in range(n+1)]
def bfs():
    global sta, n, k, end
    q = deque([(k, sta, 0)]) # 남은 리프트 탑승 횟수, 현 위치, 즐긴 시간
    while q:
        cnt, nod, tmz = q.popleft()
        if v[nod][cnt] > tmz:
            continue
        if nod == end:
            pass
        for co, nnod in godown[nod]:
            if tmz+co > v[nnod][cnt]:
                v[nnod][cnt] = tmz+co
                q.append((cnt, nnod, tmz+co))
        if cnt:
            for nnod in lift[nod]:
                if v[nnod][cnt-1] < tmz:
                    v[nnod][cnt-1] = tmz
                    q.append((cnt-1, nnod, tmz))
    return max(v[end])

def dfs(idx, val, cnt): # 노드, 시간, 올라가는 남은 횟수
    global sta, end, n, k
    for nnod in godown[idx]:
        co = godown[idx][nnod]
        if val+co > v[nnod][cnt]:
            v[nnod][cnt] = val+co
            dfs(nnod, val+co, cnt)
    if cnt:
        for nnod in lift[idx]:
            if v[nnod][cnt-1] < val:
                v[nnod][cnt-1] = val
                dfs(nnod, val, cnt-1)
    return max(v[end])

def dij():
    global sta, k, end
    heap = [(-k, 0, sta)]
    v[sta][k] = 0
    while heap:
        cnt, cost, nod = heappop(heap)
        if v[nod][cnt] > cost:
            continue
        for nnod in godown[nod]:
            co = godown[nod][nnod]
            if v[nod][cnt] > cost:
                continue
            for nnod in godown[nod]:
                co = godown[nod][nnod]
                if cost+co > v[nnod][cnt]:
                    v[nnod][cnt] = cost+co
                    heappush(heap, (cnt, cost+co, nnod))
        if cnt < 0:
            for nnod in lift[nod]:
                if v[nnod][cnt-1] < cost:
                    v[nnod][cnt-1] = cost
                    heappush(heap, (cnt+1, cost, nnod))
    return max(v[end])
'''

