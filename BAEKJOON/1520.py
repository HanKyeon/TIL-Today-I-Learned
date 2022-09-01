'''
내리막 길

0,0 시작해서 젤 우하단으로 감소하는 길로만 갈 수 있는 경우의 수

입력
세로M 가로N
높이제시, 높이는 1만 이하 자연수

출력
첫째 줄에 이동 가능한 경로의 수 H 출력. 모든 입력에 대해 H는 10억 이하 음이 아닌 정수
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

m, n = map(int, input().split())
g = [list(map(int, input().rstrip().split())) for _ in range(m)]

q = deque()
q.append((0, 0))
ans = 0
while q:
    h, w = q.popleft()
    if h == m-1 and w == n-1:
        ans += 1
        continue
    for i in range(4):
        nh, nw = h + dh[i], w + dw[i]
        if 0<=nh<m and 0<=nw<n and g[nh][nw]<g[h][w]:
            q.append((nh, nw))
print(ans)





