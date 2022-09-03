'''
최소비용 구하기

N개의 도시. 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스.
A에서 B까지 가는 버스 비용 최소화.
A에서 B까지 가는 최소비용 출력.
도시 번호는 1부터 N

입력
1이상 1000이하 n
1이상 10만이하 m
버스 정보. 출발 도착 비용. 비용 0이상 10만이하.
출발점의 도시 번호와 도착점의 도시 번호 제시.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# 다익스트라
def dijkstra(num):
    global n, end
    heap = [] # 힙
    dst[num] = 0 # 자기 자신 거리 0
    heappush(heap, (0, num)) # 힙에 넣기
    while heap:
        cost, now = heappop(heap) # now까지 비용 cost
        if dst[now] < cost: # 현재 저장된 비용보다 새로 받은 비용이 더 크면 pass
            continue
        if now == end: # 최소 비용으로 뺐는데 목표힙이라면 끝내면 됨.
            return
        for i in g[now]: # 현재 노드에서 갈 수 있는 길을 확인
            c, t = i # 현재 노드에서 t로 가는 비용 c
            nc = cost + c # t까지의 새 코스트 nc는 받아온 cost에 c를 더한 것
            if dst[t] > nc: # 만약 저장된 비용보다 작다면
                dst[t] = nc # 갱신하고
                heappush(heap, (nc, t)) # heap에 넣어준다.

n, m = int(input()), int(input())
dst = [int(10e9)]*(n+1)
g = [[] for _ in range(n+1)]
for _ in range(m):
    sta, end, cst = map(int, input().rstrip().split())
    g[sta].append((cst, end))
sta, end = map(int, input().split())
dijkstra(sta)
print(dst[end])





