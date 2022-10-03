'''
일요일 아침의 데이트

숲 탐색.
짱 예쁜 꽃 찾으러 갈 것. 사람들이 쓰레기 겁나 버림.
쓰레기를 통과해서 지나갈 수 없고, 쓰레기 옆을 지나갈 수도 없음.
숲의 지도 제시.
S는 데이트 시작 장소. F는 꽃이 있는 장소, g는 쓰레기 장소, .은 깨끗
S에서 F로 가는데, 쓰레기로 차있는 칸을 되도록 적게 지나가는 것. 가로or세로 이동 가능.
되도록 적게 지나가는 경우의 수가 여러개라면, 쓰레기 옆을 지나가는 칸의 갯수 최소로 해서 이동 예정. 만약 어떤 칸이 비어있는데, 인접한 칸에 쓰레기가 있으면 쓰레기 옆을 지나는 것. s, f는 카운트 x

입력
n, m  제시. 3이상 50이하 S F g . 제시. S는 모서리, F는 모서리 아님. 하나만 제시.

출력
최적의 방법으로 숲을 지나갔을 때, 지나가는 쓰레기의 최소 갯수 출력, 공백으로 구분 한 후에 쓰레기 옆을 지나가는 칸의 갯수 출력.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def dij():
    global n, m
    while heap:
        cg, ng, h, w = heappop(heap)
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and not v[nh][nw]:
                if g[nh][nw] == 'F':
                    return [cg, ng]
                elif g[nh][nw] == '.':
                    v[nh][nw] = 1
                    heappush(heap, (cg, ng+dp[nh][nw], nh, nw))
                elif g[nh][nw] == 'g':
                    v[nh][nw] = 1
                    heappush(heap, (cg+1, ng, nh, nw))

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
heap = []
v = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if g[i][j] == 'S':
            heap.append((0, 0, i, j))
            v[i][j] = 1
        elif g[i][j] == 'g':
            for dh, dw in mov:
                nh, nw = i+dh, j+dw
                if 0<=nh<n and 0<=nw<m:
                    dp[nh][nw] = 1
print(*dij())





