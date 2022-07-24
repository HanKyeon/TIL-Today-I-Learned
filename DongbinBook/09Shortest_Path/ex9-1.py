'''
간단한 다익스트라 알고리즘 소스코드

가장 기초적인 데이크스트라 코드이다.
d테이블 : 시작 노드로부터 index노드까지의 최단거리.
g그래프 : index노드에서 (도착노드, 거리) 간선 튜플 리스트를 리스트로 표현
v테이블 : 노드들의 방문여부. index 노드를 돌았는지 확인하여 중복작업 방지

'''

import sys
input = sys.stdin.readline # input을 readline으로 정의한듯?
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정
# n, m 입력
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
# 현재 d 테이블에서 방문하지 않은, 거리가 가장 가까운 노드 반환
def get_smallest_nod() :
    min_value = INF # 가장 적은 거리를 뽑아야 하므로, 비교군을 가장 큰 값으로 우선 지정
    index = 0 # 0번 노드는 없으니 절대 도달 못하므로 일단 0으로 설정
    # 1부터 n까지 인덱스가 노드번호이므로 그만큼 순회
    for i in range(1, n+1) :
        # 거리가 현 최솟값보다 낮고, 방문하지 않았다면
        if d[i] < min_value and not v[i] :
            min_value = d[i] # 최솟값 갱신하고
            index = i # 그 최솟값 인덱스 반환
    # d테이블을 순환하며 d테이블의 값이 가장 낮은 index 반환.
    return index

# 다익스트라 시작. 시작점 인덱스가 파라미터.
def dijkstra(start) :
    # 자기 자신까지의 거리는 0 하나 뿐이니 직접 입력 및 방문 처리
    d[start] = 0
    c[start] = True
    # g[j]는 j인덱스에서 출발하는 간선 모음
    # d[j[0]] = d[도착 노드 인덱스] = 도착노드 인덱스까지의 거리
    # j[1] = 거까지 가는 거리.
    # 따라서 d[j[0]] = j[1]은 노드에서 최소거리 잡아주는 것
    for j in g[start] :
        d[j[0]] = j[1]

    # 시작 노드 뺀 n-1번 반복할 것. 0번 노드는 쭉 INF이므로
    # 거리순에 따라 순회하므로 모든 노드 순회 가능
    for i in range(n-1) :
        # 시작 노드에서 최단 거리가 가장 짧은 노드 추출 및 방문
        now = get_smallest_nod()
        v[now] = True
        # 방문한 현재 노드와 연결된 다른 노드 확인.
        for j in g[now] : # 최단으로 이동한 노드의 간선 확인
            cost = d[now] + j[1] # 이동에 들어가는 비용은 현재 노드까지 요구비용 + 간선의 비용
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < d[j[0]] : # 그 비용이 기존 비용보다 낮으면
                                # 여기서 d[j[0]] == now에서 출발하여 도착하는 노드까지의 비용
                                # 즉, 현재 테이블에 적혀있는 최솟값과 
                                # now노드를 경유해 j[0]에 이동하는 거리를 비교해서
                                # 현재 최솟값보다 작다면 
                d[j[0]] = cost # 그 값을 넣어준다. min으로 해도 될듯?
# 실행
dijkstra(startnod)
# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1) :

    if d[i] == INF :
        print("INFINITY")
    else :
        print(d[i])

