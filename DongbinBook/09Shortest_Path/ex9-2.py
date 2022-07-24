'''
개선된 다익스트라 알고리즘 소스코드

다익스트라는 모든 노드를 확인한다.
최단 거리가 가장 짧은 노드를 선택 할 때 순회해야 하고, 여러번 순회한다.
그 중에서 최단거리가 가장 짧은 노드를 선택 하는 기능 부분을
우선순위 큐(Heap Queue) 라는 자료구조를 이용해 대체 할 수가 있다.

해당 방법을 적용한 소스코드이다.
'''
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = int(input().split)
# 시작 노드 입력
startnod = int(input())
# index노드에서 (도착노드, 거리) 간선 튜플 리스트를 리스트로 표현
g = [[] for i in range(n + 1)]
# 노드들의 방문여부. index 노드를 돌았는지 확인하여 중복작업 방지
v = [False] * (n + 1)
# 시작 노드로부터 index노드까지의 최단거리.
d = [INF] * (n + 1)

# 모든 간선 정보를 g테이블에 입력
for _ in range(m) :
    # 출발 a번노드 도착 b노드 거리 c
    a, b, c = map(int, input().split())
    # a 인덱스에 있는 리스트에 (도착점b, 값c)를 튜플 형태로 입력
    g[a].append((b, c))

# 다익스트라
def dijkstra(start) :
    # 우선순위 큐를 통해 순서를 받을 q[]
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 q에 삽임
    heapq.heappush(q, (0, start))
    d[start] = 0

    # q가 비어있지 않다면 True 비어있다면 False. 빌 때까지 반복해라
    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보를 빼낸다.
        di, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시한다.
        # 같은 노드라면 거리순이 짧을 때부터 우선순위 큐에 정리되므로
        # di가 d[now]보다 크면 무시한다. 또 실제로 거리가 더 길다는 것이니 무시해도 될듯.
        if d[now] < di :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        # g테이블을 통해 now와 에서 출발하는 노드들 확인.
        for i in g[now] :
            # di 현재 노드까지 든 코스트에 i[1] now에서 이동하는데 필요한 코스트
            cost = di + i[1]
            # 현재 노드들을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우 heqppush를 통해 q에 넣어준다.
            # 코스트가 갱신 될 때 push해서 넣어준다.
            if cost < d[i[0]] :
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 실행
dijkstra(startnod)
# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1) :

    if d[i] == INF :
        print("INFINITY")
    else :
        print(d[i])



