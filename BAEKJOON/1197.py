'''
최소 스패닝 트리

그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
최소 스패닝 트리는 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

입력
v, e 1이상1만이하 1이상10만이하 제시
e개 줄에 간선 정보 a, b, c 제시. a번 정점과 b번 정점이 가중치 c인 간선으로 연결되어 있다는 의미이다. c는 음수일 수도 있으며, 절댓값이 100만을 넘지 않는다. 그래프의 정점은 1번부터 v번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치는 -21억 뭐시기 이상 21억 뭐시기 이하

출력
최소 스패닝 트리의 가중치 출력
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline


v, e = map(int, input().rstrip().split())
vst = [0]*(v+1)
eli = [[] for _ in range(v+1)]
heap = [[0, 1]]
for i in range(e):
    a, b, c = map(int, input().rstrip().split())
    eli[a].append((c, b))
    eli[b].append((c, a))
cnt = 0 # cnt가 아닌 sum(vst)로 하면 시간 초과. sum 시간이 걸려서 그런듯?
dp = [0] * (v+1)
while heap:
    if cnt == v:
        break
    c, n = heappop(heap)
    if not vst[n]:
        vst[n] = 1
        dp[n] = c
        cnt += 1
        for i in eli[n]:
            heappush(heap, i)
print(sum(dp))





'''
Kruskal 알고리즘 이용
1. root를 저장하는 Vroot 배열을 생성한다. (여기서 root는 연결요소중 가장 작은 값, 처음에는 자기 자신을 저장)
2. 간선들(Elist)을 가중치 기준으로 정렬한다.
3. 간선들이 이은 두 정점을 find함수를 통해 두 root(sRoot, eRoot)를 찾는다.
4. 두 root가 다르다면 큰 root값을 작은 root값으로 만들어 연결되게 해준다.
5. 가중치를 더한다.

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))

Elist.sort(key=lambda x: x[2])


def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w

print(answer)
'''

'''
Prim 알고리즘
1. visited : 노드 방문 여부.
2. Elist : 간선 저장.
3. heap : 현재 그래프에서 가장 짧은 경로를 고를 때. 현재 그래프에서 가장 짧은 간선을 골라 방문하지 않은 정점이라면 선택.

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [False]*(V+1)
Elist = [[] for _ in range(V+1)]
heap = [[0, 1]]
for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])

answer = 0
cnt = 0
while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)

print(answer)
'''
