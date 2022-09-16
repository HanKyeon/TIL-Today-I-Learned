'''
컨택트

비상 연락망과 시작하는 당번에 대한 정보 제시. 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하시오.

BFS 깊이 넣어서 젤 깊은 애들 중 최대 번호 출력

1. 1이상 100이하 번호
2. 빵꾸날 수 있음.
3. BFS
4. BFS
5. 방문처리.
6. 방향성 그래프.

입력
시작 도착 시작 도착 시작 도착...
여러개 나올 수 있음.
'''
from collections import deque

for testcase in range(1, 11):
    n, stn = map(int, input().rstrip().split())
    nl = list(map(int, input().rstrip().split()))
    g = [[] for _ in range(101)] # 그래프 정보
    v = [0]*101 # 방문
    for i in range(0, n, 2):
        sta, end = nl[i], nl[i+1]
        g[sta].append(end) # 시작 노드에 도착 노드 추가
    q = deque([(stn, 0)]) # 노드, 깊이
    v[stn] = 1 # 방문처리
    dpm = [0]*101 # depth 중 가장 큰 노드 기록 할 그래프
    while q: # q 빼면서
        nod, dep = q.popleft() # 노드랑 깊이
        dpm[dep] = max(dpm[dep], nod) # depth 중 가장 큰 노드 갱신
        for i in g[nod]: # 그래프 탐색
            if v[i]: # 방문되어 있다면 다음꺼
                continue
            v[i] = 1 # 방문처리
            q.append((i, dep+1)) # 큐에 넣기
    print(f"#{testcase} {dpm[dep]}")

















