'''
전보

N개의 도시. 통로가 있어야 한다. 통로는 단방향

C 도시에 위급상황. 최대한 많은 도시로 메시지 보내야 한다.
각 도시 사이에 설치된 통로를 거쳐 최대한 많이 퍼져나갈 것.
도시와 통로의 정보가 주어졌을 때 C에서 보낸 메시지를 받게되는 도시는 
총 몇개이며 도시들이 모두 메시지를 받는데까지 걸리는 시간은?

1부터 3만까지의 N, 1부터 20만까지의 M, 1부터 N까지의 C
둘째줄부터 m+1번째 줄에 걸쳐서 통로에 대한 정보 X,Y,Z
특정도시 X에서 Y로 이어지는 통로와 메시지 전송시간Z

다익스트라 알고리즘 사용 가능. N과 M의 범위가 매우 크기 때문에
우선순위큐를 이용한 다익스트라 알고리즘 짜야한다.
'''
# 임포트
import heapq
import sys
# input을 readline으로 변경 및 INF 값 설정
input = sys.stdin.readline
INF = int(1e9)
# n, m, 시작노드 입력
n, m, start = map(int, input().split())
# 그래프 초기화. 다익스트라 알고리즘이므로 노드(인덱스)별로 연결된 간선 데이터 테이블
g = [[] for i in range(n + 1)]
# 최단거리를 기록하는 테이블.
distance = [INF] * (n + 1)
# x에서 y까지 z의 비용이 드는 간선들 죄다 기록
for _ in range(m) :
    x, y, z = map(int, input().split())
    g[x].append((y, z))
# 다익스트라 함수
def dijkstra(start) :
    q = []
    # 시작 노드에서 시작 노드로는 거리가 0이다를 큐에 삽입.
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # q가 비어있지 않다면 반복
    while q :
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in g[now] :
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 값 갱신
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
# 다익스트라 수행
dijkstra(start)
# 도달 할 수 있는 노드의 갯수
c = 0
# 도달 할 수 있는 노드 중에서 가장 멀리 있는 노드와의 최단 거리
maxDistance = 0

for d in distance :
    # 도달 할 수 있다면, maxD를 초기화
    if d != INF :
        c += 1
        maxDistance = max(maxDistance, d)
# 시작 노드로의 이동은 빼야 하기에 c-1을 출력
print(c - 1, maxDistance)



