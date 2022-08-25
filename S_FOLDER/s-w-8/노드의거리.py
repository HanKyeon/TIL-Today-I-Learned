'''
노드의 거리

노드갯수V 간선갯수E
두 노드의 거리

입력
테케T
V E
간선 제시.
출발S 도착G

출력
#T S에서 G까지 거리
'''
from collections import deque

def bfs(sta, end, c): # bfs
    q = deque() # 큐
    q.append((sta, c)) # 추가
    v[sta] = 1 # 방문
    while q: # q 다 뺄 때까지
        s, c = q.popleft() # 시작노드, 거리
        for i in g[s]: # 시작노드에서 이동 가능한 노드들 돌면서
            if v[i] == 0: # 방문 안했으면
                if i == end: # 근데 그게 도착점이면
                    return c+1 # 리턴함
                v[i] = 1 # 아니면 방문처리
                q.append((i, c+1)) # 큐에 추가

for testcase in range(1, int(input())+1):
    n, m = map(int, input().split()) # n, m 입력
    v = [0]*(n+1) # 방문
    g = [[] for _ in range(n+1)] # 간선 그래프
    for _ in range(m): # m번 반복
        a, b = map(int, input().split()) # 노드 두개
        g[a].append(b) # 양
        g[b].append(a) # 방향
    st, en = map(int, input().split()) # 시작 도착노드
    ans = bfs(st, en, 0)
    if ans == None: # 길 없으면
        ans = 0 # 0이다
    print(f"#{testcase} {ans}") # 출력

