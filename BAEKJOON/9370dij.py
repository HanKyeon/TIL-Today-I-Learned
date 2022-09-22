'''
미확인 도착지

s 지점에서 출발, 목적지 후보들 중 하나가 그들의 목적지. 최단거리로 갈 것.
간선에서 흔적을 찾음. 아마 노드 두개를 시작점으로 해보라는 것 같음.

입력
테케T
n, m, t 제시. 2이상 2000이하, 1이상 5만이하, 1이상 100이하. 각각 교차로노드, 도로, 목적지 후보의 갯수.
s, g, h 제시. s는 출발지, g, h는 교차로.
m개의 각 줄마다 a, b, d 제시. a와 b 사이에 길이 d의 양방향 도로.
t개의 줄에 정수 x 제시. 목적지 후보들. 서로 다른 위치이며 s와 다름.
노드 사이 도로는 많아봐야 1개. m개 줄 중에서 m, h 사이의 도로를 나타낸 것이 존재. 이 도로는 목적지 후보들 중 적어도 1개로 향하는 최단 경로이다.

출력
테케마다 입력에서 주어진 목적지 후보들 중 불가능한 경우를 제외한 목적지들을 공백분리 오름차순 출력.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij(idx):
    dst = [int(10e9)]*(n+1)
    dst[idx] = 0
    heap = [(0, idx)]
    while heap:
        sumc, nod = heappop(heap)
        if sumc > dst[nod]:
            continue
        for i in g[nod]:
            cost, nnod = i
            if dst[nnod] > sumc+cost:
                dst[nnod] = sumc+cost
                heappush(heap, (sumc+cost, nnod))
    return dst

for tc in range(int(input())):
    n, m, t = map(int, input().rstrip().split())
    sta, nd1, nd2 = map(int, input().rstrip().split())
    g = [[] for _ in range(n+1)]
    dst = [int(10e9)]*(n+1)
    for _ in range(m):
        a, b, d = map(int, input().rstrip().split())
        g[a].append((d, b))
        g[b].append((d, a))
    for i in g[nd1]:
        if i[1] == nd2:
            di = i[0]
            break
    endz = [int(input()) for _ in range(t)]
    dst = dij(sta)
    no1dst = dij(nd1)
    no2dst = dij(nd2)
    ans = []
    for i in endz:
        if dst[i] == dst[nd1]+di+no2dst[i] or dst[i] == dst[nd2]+di+no1dst[i]:
            ans.append(i)
    ans.sort()
    print(*ans)




'''
# 시간초과 날거 같더라니 쯧쯧
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, m, t = map(int, input().rstrip().split())
    sta, nd1, nd2 = map(int, input().rstrip().split())
    g = [[] for _ in range(n+1)]
    dst = [int(10e9)]*(n+1)
    for _ in range(m):
        a, b, d = map(int, input().rstrip().split())
        g[a].append((d, b))
        g[b].append((d, a))
    endz = [int(input()) for _ in range(t)]
    heap = [(1, 0, sta)] # 중요 간선 방문 여부. 방문 시 0으로 만들어서 우선 순위 처리 할 것.
    dst[sta] = 0
    rdst = {}
    while heap:
        fla, sumc, nod = heappop(heap)
        if sumc > dst[nod]:
            continue
        if fla == 0 and nod in endz:
            if not rdst.get(nod, 0):
                rdst[nod] = sumc
            if len(rdst) == len(endz):
                break
        for i in g[nod]:
            cost, nnod = i
            if dst[nnod] >= sumc+cost:
                dst[nnod] = sumc+cost
                if (nnod == nd1 and nod == nd2) or (nnod == nd2 and nod == nd1):
                    heappush(heap, (fla-1, sumc+cost, nnod))
                else:
                    heappush(heap, (fla, sumc+cost, nnod))
    ans = []
    for i in rdst.keys():
        if rdst[i] == dst[i]:
            ans.append(i)
    ans.sort()
    print(*ans)
'''







'''
2
5 4 2
1 2 3
1 2 6
2 3 2
3 4 4
3 5 3
5
4
6 9 2
2 3 1
1 2 1
1 3 3
2 4 4
2 5 5
3 4 3
3 6 2
4 5 4
4 6 3
5 6 7
5
6
'''





