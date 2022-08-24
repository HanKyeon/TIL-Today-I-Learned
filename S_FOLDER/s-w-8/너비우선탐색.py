




from collections import deque

for testcase in range(1, int(input())+1):
    # 입력
    v, e = map(int, input().split()) # 노드 간선
    g = [[] for _ in range(v+1)] # 간선 그래프
    for i in range(e): # 그래프 작업
        a, b = map(int, input().split())
        g[a].append(b)
    g = list(map(sorted, g)) # 그래프 내부 정렬
    # bfs
    q = deque() # 큐 선언
    q.append(1) # 시작점 삽입
    v = [1]+[0]*v # 방문 확인
    v[1] = 1 # 1번 노드 방문처리
    ans = [] # 정답
    while q: # 간선으로 이어진 곳 다 방문 할 때까지
        n = q.popleft() # 큐 가장 왼쪽에서 빼서
        ans.append(n) # 정답 넣고
        for i in g[n]: # 그 번호 그래프 훑어서
            if v[i] == 0: # 방문 안된거
                v[i] = 1 # 방문처리 후에
                q.append(i) # q에 또 넣어라.
    # 출력
    print(f"#{testcase}", end=' ') # 출
    print(*ans) # 력



