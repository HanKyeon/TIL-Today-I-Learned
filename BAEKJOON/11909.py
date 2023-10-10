'''
배열 탈출

2초 256메가
2차원 배열. 1이상 222이하 정수
n, n에 출구
우 혹은 하로만 이동 가능, 더 낮은 곳으로 이동 가능. 버튼 누르면 1 증가하고 1원 들어감. 돈 적게 탈출할 것.

입력
n 제시
그래프 제시

출력
탈출하기 위한 최소 비용 출력
'''
import sys
def input(): return sys.stdin.readline().rstrip()
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if 0>i-1 and 0>j-1: continue
        oi, oj = sys.maxsize, sys.maxsize
        if 0<=i-1: oi = dp[i-1][j]+(0 if g[i][j]<g[i-1][j] else g[i][j]-g[i-1][j]+1)
        if 0<=j-1: oj = dp[i][j-1]+(0 if g[i][j]<g[i][j-1] else g[i][j]-g[i][j-1]+1)
        dp[i][j] = min(oi, oj)
print(dp[n-1][n-1])

'''
# 시간초과. 시간 될 것 같이 생겼는데 안되네
import sys
from heapq import heappop, heappush
def input(): return sys.stdin.readline().rstrip()

mov = [(0,1), (1,0)]

def dij():
    global n
    cst = [[sys.maxsize]*n for _ in range(n)]
    cst[0][0] = 0
    while heap:
        cost, h, w = heappop(heap)
        if cst[h][w] < cost: continue
        if h==w==n-1: return cost
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n:
                co = g[nh][nw]-g[h][w]+1
                if co < 1:
                    if cst[nh][nw] > cost: cst[nh][nw] = cost; heappush(heap, (cost, nh, nw)); continue
                if cst[nh][nw] > cost+co: cst[nh][nw] = cost+co; heappush(heap, (cost+co, nh, nw))

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
heap = [(0, 0, 0)]
print(dij())
'''
