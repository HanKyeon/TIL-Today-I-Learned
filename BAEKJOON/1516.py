'''
게임 개발

세준 크래프트 개발.
건물을 짓는데 걸리는 최소 시간을 이용해 게임을 근사.
어떤 건물을 위해 선행 건물이 필요 할 수 있따.
여러개 건물 동시짓기 가능.
자원 무제한, 딜레이 없음.

입력
건물 종류 1~500
건물 짓는데 걸리는 시간, 건물을 짓기 위해 먼저 지어져야 하는 건물들의 번호. 건물 번호는 1~N, 각줄은 -1로 끝남.
각 건물을 짓는데 걸리는 시간은 10만보다 작거나 같은 자연수. 모든 건물 건설 가능.

출력
N개의 각 건물이 완성되기까지 걸리는 최소 시간 출력.
'''
from collections import deque

n = int(input()) # 입력
reqn = [0]*(n+1) # 요구 노드 수
g = [[] for _ in range(n+1)] # 그래프 간선
t = [0]*(n+1) # 건축 시간 넣을 것
for i in range(1, n+1):
    a = list(map(int, input().split())) # 입력
    t[i] = a.pop(0) # 첫번째꺼는 건축에 걸리는 시간
    a.pop() # -1 제거
    while a: # 나머지는
        b = a.pop()
        g[b].append(i) # 전부 다 거기서 여기로 뻗어오는 간선이다.
        reqn[i] += 1 # 요구 노드 증가
rt = t[:] # 총 걸리는 시간 메모용.

# 위상정렬
q = deque() # 큐
for i in range(1, n+1): # 요구 노드 없는 노드 삽입
    if reqn[i] == 0:
        q.append(i)

while q: # 다 훑을 때까지
    nn = q.popleft() # 빼서 봐라
    for i in g[nn]: # 거기서 뻗는 노드 있으면
        reqn[i] -= 1 # 받는 노드의 요구노드 하나 감소
        rt[i] = max(rt[i], rt[nn]+t[i]) # 거기 이미 기록된 총 걸리는 시간 vs nn까지 총 걸리는 시간 + 거기 걸리는 시간 중 큰 값이 건물 짓는데 걸리는 시간.
        if reqn[i] == 0: # 요구 노드 없으면
            q.append(i) # 추가해서 살펴라

for i in range(1, n+1): # 출력
    print(rt[i])



