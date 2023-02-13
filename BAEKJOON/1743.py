'''
음식물 피하기

제일 큰 음식물의 크기를 구해라.

입력
세로 가로 음쓰 n, m, k 제시. k개 줄에 음쓰 좌표 제시.

출력
음쓰 중 가장 큰 음쓰 크기 출력.
'''
import sys
from collections import deque
input = sys.stdin.readline

mov = [(-1,0),(0,1),(1,0),(0,-1)]

def find(h, w):
    q = deque([(h, w)])
    g[h][w] = 0
    ret = 1
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw]:
                ret += 1
                g[nh][nw] = 0
                q.append((nh, nw))
    return ret

n, m, k = map(int, input().rstrip().split())
g = [[0]*m for _ in range(n)]
for _ in range(k):
    h, w = map(int, input().rstrip().split())
    g[h-1][w-1] = 1
ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j]:
            ans = max(ans, find(i, j))
print(ans)


