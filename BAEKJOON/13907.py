'''
세금

통행료 합이 가장 적은 경로로 이동하려 한다. 양방향 도로.
세금 인상이 있다. 여러 단계 걸쳐서 올린다. 모든 도로의 통행료가 동시에 a만큼 오르게 된다. 통행료가 변할 수 있다.
최소 통행료와 세금이 오를 때마다 최소 통행료를 구해라.

입력
n, m, k 제시. 도시 도로 세금인상 횟수
정수 s와 d 제시. 출발, 도착 도시. 도시는 1번부터 존재.
m개 줄 세 정수 a, b, c 제시.
k개 줄 정수 p 제시. k번째에 인상되는 세금 의미.
s에서 d로 이동할 수 없는 경우 없음.

출력
세금이 오르기 전의 최소 통행료 출력
k번째 세금이 올랐을 때 최소 통행료 출력
'''
'''
- 경로 최소 갯수로 해야하나, 가중치 최소로 해야하나... 둘 다 해야하나...
'''
import sys
from heapq import heappop, heappush
from math import inf
input = sys.stdin.readline

def dij():
    global n, s, e
    heap = [(0, 0, s)] # 가중치, 방문 횟수, 노드
    while heap:
        cost, cnt, nod = heappop(heap)
        if min(dp[nod][:cnt+1]) < cost:
            continue
        for co, nnod in g[nod]:
            if cnt < n and cost+co < dp[nnod][cnt+1]:
                dp[nnod][cnt+1] = cost+co
                heappush(heap, (cost+co, cnt+1, nnod))

n, m, k = map(int, input().rstrip().split())
s, e = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
dp = [[inf]*(n+1) for _ in range(n+1)]
dp[s][0] = 0
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
dij()
print(min(dp[e]))
for _ in range(k):
    amt = int(input())
    ans = inf
    for j in range(n+1):
        if dp[e][j] == inf:
            continue
        dp[e][j] += amt*j
        if dp[e][j] < ans:
            ans = dp[e][j]
    print(ans)

'''
# 빠른 코드

import sys
import heapq
input = sys.stdin.readline
# sys.stdin = open("BOJ/input.txt", "r")
INF = 987654321

def dijkstra():

    distance = [[INF] * N for _ in range(N+1)]
    distance[S][0] = 0
    hq = []
    heapq.heappush(hq, (0, S, 0))

    while hq:
        flag = False
        cur_c, cur_v, passed_cnt = heapq.heappop(hq)

        if passed_cnt == N-1: continue
        
        for i in range(passed_cnt + 1):
            if distance[cur_v][i] < cur_c:
                flag = True
                break
        if flag: continue

        for new_v, new_c in road[cur_v]:
            next_c = cur_c + new_c
            if distance[new_v][passed_cnt + 1] > next_c:
                distance[new_v][passed_cnt + 1] = next_c
                heapq.heappush(hq, (next_c, new_v, passed_cnt + 1))

    return distance[D]


N, M, K = map(int, input().split())
S, D = map(int, input().split())

road = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    road[a].append((b, w))
    road[b].append((a, w))

tax_lst = [0]
next_tax = 0
for _ in range(K):
    next_tax += int(input())
    tax_lst.append(next_tax)

distance_D = dijkstra()

answers = []
max_cnt = N-1
for tax in tax_lst:
    min_v = INF
    for passed_cnt in range(1, max_cnt+1):
        cost = distance_D[passed_cnt] + (passed_cnt*tax)
        if min_v > cost:
            min_v = cost
            max_cnt = passed_cnt
    answers.append(min_v)

for ans in answers:
    print(ans)
'''

'''
# 빠른 코드

import sys
input=sys.stdin.readline
from math import inf
n,m,k=map(int,input().split())
road={}
d={x:{} for x in range(1,n+1)}
s,e=map(int,input().split())

for _ in range(m):
  a,b,w=map(int,input().split())
  if(b in d[a].keys()):
    d[a][b]=min(d[a][b],w)
  else:
    d[a][b]=w
  if(a in d[b].keys()):
    d[b][a]=min(d[b][a],w)
  else:
    d[b][a]=w

dist=[inf for _ in range(n+1)]
dist[s]=0
can={s:[]}
length=1
real={}

while(True):
  new_can={}
  for city in can:
    for connected in d[city].keys():
      if(connected==e):
        if(length in real):
          real[length]=min(real[length],dist[city]+d[city][connected])
        else:
          real[length]=dist[city]+d[city][connected]
      else:
        if(dist[city]+d[city][connected]<dist[connected]):
          if(connected not in new_can): new_can[connected]=[]
          new_can[connected].append(dist[city]+d[city][connected])
  if not(new_can):
    break
  for x,y in new_can.items():
    for z in y:
        dist[x]=min(dist[x],z)
  can=new_can
  length+=1
print(min(real.values()))
r=list(real.keys())
for _ in range(k):
  ad=int(input())
  for x in r:
    real[x]+=x*ad
  print(min(real.values()))
'''

'''
import sys
from heapq import heappop, heappush
from math import inf
input = sys.stdin.readline

def dij():
    global n, s, e
    heap = [(0, 0, s)] # 가중치, 방문 횟수, 노드
    while heap:
        cost, cnt, nod = heappop(heap)
        fla = False
        for i in range(cnt):
            if dp[nod][i] < cost:
                fla = True
                break
        if fla or dp[nod][cnt] < cost:
            continue
        for co, nnod in g[nod]:
            if cnt < n and cost+co < dp[nnod][cnt+1]:
                dp[nnod][cnt+1] = cost+co
                heappush(heap, (cost+co, cnt+1, nnod))

n, m, k = map(int, input().rstrip().split())
s, e = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
dp = [[inf]*(n+1) for _ in range(n+1)]
dp[s][0] = 0
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
dij()
print(min(dp[e]))
for _ in range(k):
    amt = int(input())
    ans = inf
    for j in range(n+1):
        if dp[e][j] == inf:
            continue
        dp[e][j] += amt*j
        if dp[e][j] < ans:
            ans = dp[e][j]
    print(ans)
'''
