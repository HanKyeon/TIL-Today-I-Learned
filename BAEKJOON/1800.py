'''
인터넷 설치

학생들은 1번부터 n번까지 번호. P개의 쌍만 연결 가능. 서로 연결하는데 비용이 들어감.
1번은 인터넷 가능. n번까지 연결하는게 목표. 나머지는 무관.
k개의 인터넷 선은 공짜. 남은 것 중 가격이 비싼 것에 대해서만 가격을 받을 것. 최소값.

입력
n, m, k 제시. 학생n 간선m 공짜갯수k
p개 줄 a, b, c 제시. a와 b 연결에 c값

출력
내야하는 최소의 돈 출력.
1번과 n번을 잇는 것이 불가능 하다면 -1 출력
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

# 다익스트라. 근데 카운트로 하는
def dij(val):
    global n
    freeCnt = [int(10e9)] * (n+1) # 꽁짜 쓴 갯수
    freeCnt[1] = 0 # 1번 초기화
    heap = [(0, 1)] # 힙
    while heap:
        nodc, nod = heappop(heap) # 공짜 카운트, 노드
        if freeCnt[nod] < nodc: # 덜 써서 갈 수 있으면 continue
            continue
        if nod == n: # n이면
            return nodc # 즉시 공짜 카운트 횟수 리턴
        for co, nnod in g[nod]:
            if co > val: # mid 값보다 크면서
                if freeCnt[nnod] > nodc+1: # 공짜 썼을 때 카운트가 더 적음녀
                    freeCnt[nnod] = nodc+1 # 갱신
                    heappush(heap, (nodc+1, nnod)) # 푸쉬
                continue
            if freeCnt[nnod] > nodc: # 작으면
                freeCnt[nnod] = nodc # 갱신
                heappush(heap, (nodc, nnod)) # 푸쉬
    return -1 # 못가면 -1

n, m, k = map(int, input().rstrip().split()) # 노드, 간선, 공짜
g = [[] for _ in range(n+1)] # 그래프
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))

# 이분 탐색
lft, rgt = 0, 1000001
ans = int(10e9)
while lft <= rgt:
    mid = (lft + rgt) // 2
    nc = dij(mid)
    if 0 <= nc <= k: # 갈 수 있으며 공짜일 때 더 작은 값 찾아보기
        ans = mid
        rgt = mid-1
        continue
    lft = mid+1 # 못가거나 공짜 갯수 넘으면 더 큰 값 찾기
if ans == int(10e9): # ans 갱신 안됐으면 -1
    print(-1)
else: # 갱신 됐으면 ans 출력
    print(ans)





'''
# 일반 다익
def dij():
    global n
    dst = [inf] * (n+1)
    dst[1] = 0
    heap = [(0, 1, [])]
    while heap:
        cost, nod, costs = heappop(heap)
        ncosts = costs[:]
        if dst[nod] < cost:
            continue
        if nod == n:
            return costs
        for co, nnod in g[nod]:
            costco = cost+co
            if costco < dst[nnod]:
                dst[nnod] = costco
                heappush(ncosts, -co)
                # if len(ncosts) > k+1:
                #     heappop(ncosts)
                heappush(heap, (costco, nnod, ncosts))
    return -1
'''
