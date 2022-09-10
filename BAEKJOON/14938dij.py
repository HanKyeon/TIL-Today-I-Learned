'''
서강 그라운드

배그한다.
지역 별 양방향 통행 가능.

떨어진 지역 내 수색ㄱ 범위 m 이내의 모든 지역의 아이템 습득 가능. 얻을 수 있는 아이템의 최대 갯수.

입력
1이상 100이하 n 수색범위 m 1이상 15이하 길의 갯수 1이상 100이하
각 구역의 아이템 수
양방향 두 지역, 길의 거리 제시.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij(sta): # 데이크스트라.
    global ans
    heap = [(0, sta)] # 최소힙
    dst = [int(10e9)] * (n+1) # 거리
    dst[sta] = 0 # 시작지점 거리 초기화
    while heap:
        cost, now = heappop(heap) # 여태까지 소모량, 현재 노드
        if cost > dst[now]: # 현재 들고 온 소모량잉 현재 기록된 값보다 크면 패스
            continue
        for i in g[now]: # 들고 온 노드의 간선 확인
            co, nod = i # 각 간선의 비용, 도착지
            if cost + co < dst[nod]: # 현재 비용에 간선 비용 합한게 그 노드 값보다 작다면
                dst[nod] = cost + co # 갱신 해주고
                heappush(heap, (cost + co, nod)) # 힙에 추가
    ret = 0
    for i in range(1, n+1): # 정답 갱신
        if dst[i] <= m:
            ret += il[i]
    ans = max(ans, ret)



n, m, r = map(int, input().rstrip().split())
il = [0] + list(map(int, input().rstrip().split()))
g = [[] for _ in range(n+1)]
for _ in range(r): # 그래프 만들기.
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
ans = 0
for i in range(1, n+1): # 모든 노드에 대해 다이크 스트라.
    dij(i)
print(ans)







