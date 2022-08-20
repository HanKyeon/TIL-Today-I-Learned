'''
ACM Craft

건물 짓는 순서가 정해져 있지 않다. 1세트와 2세트에 건물 짓는 순서가 다를 수 있다.
건설까지 걸리는 시간이 있다.
특정 건물을 지을 수 있는 최소 시간.
동시에 건축이 가능하다!!!!!!!!!

입력
테케T
건축물 갯수 N 규칙 갯수 M
짓는 시간 N개
규칙들
규칙들
건설해야 할 건물 번호 W

출력
건물 W를 짓는데 걸리는 최소 시간
'''

# 위상정렬 했다. DFS로도 맞는 답이 나올 수 있다고는 생각하는데, 시간이 너무 오래 걸린다고 한다.
from collections import deque
import sys
input = sys.stdin.readline

def ts(num):
    global n # n 쓰려고
    q = deque() # 덱 씀
    for i in range(1, n+1):
        if reqn[i] == 0: # 요구 노드가 0이라면
            q.append(i) # 추가하고
            v[i] = 1 # 방문처리
    while q: # q가 빌 때까지
        nn = q.popleft() # 맨앞에서 빼라.
        for i in g[nn]: # 그 숫자가 갈 수 있는 노드들 확인
            tl[i] = max(tl[i], otl[i] + tl[nn]) # 그때까지 걸리는 시간 갱신. 현재 걸리는 시간과 이번에 걸리는 시간 중 긴 것으로.
            reqn[i] -= 1 # 요구 노드 하나 빼줌
            if reqn[i] == 0 and v[i] == 0: # 요구 노드가 0이고 방문 안했으면
                q.append(i) # 추가,
                v[i] = 1 # 방문처리
    return tl[num] # 다 했으면 반환

for _ in range(1, int(input())+1):
    n, m = map(int, input().split()) # 입력
    otl = [0] + list(map(int, input().split())) # original time list. 건물 짓는 시간이 필요 할 때 씀.
    tl = otl[:] # 그 노드까지 걸리는 시간 조작용도.
    reqn = [0] * (n+1) # 요구 노드가 몇개인지 require nodes
    v = reqn[:] # 방문처리용.
    g = [[] for _ in range(n+1)] # 출발-시작 노드 받을 것
    for _ in range(m):
        sta, end = map(int, input().split()) # 시작노드 도착노드
        reqn[end] += 1 # 도착노드의 요구되는 노드 수 증가
        g[sta].append(end) # 시작 노드에서 출발 할 수 있는 노드에 추가.
    w = int(input()) # 지어야 하는 건물
    print(ts(w)) # 출력




















'''
def dfl(num, t):
    global ans, tl
    if not reqn[num]:
        if ans < t:
            ans = t
        return
    for i in reqn[num]:
        dfl(i, t+tl[i])

for testcase in range(1, int(input())+1):
    n, m = map(int, input().split())
    tl = [0] + list(map(int, input().split()))
    # g = [list(map(int, input().split())) for _ in range(m)]
    reqn = [[] for _ in range(n+1)]
    # v = [0] * (n+1)
    for i in range(m):
        sta, end = map(int, input().split())
        reqn[end].append(sta)
    w = int(input())
    ans = 0
    dfl(w, tl[w])
    print(ans)
'''

