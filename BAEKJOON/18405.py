'''
경쟁적 전염

N*N 시험관.
1번부터 k번까지의 바이러스 존재.
초마다 번호 작은거 먼저 1칸 씩 증식.
S초 후 x, y에 존재하는 바이러스 종류 출력. 없으면 0 x는 행 y는 열

입력
n, k 제시. n은 1이상 200이하 k는 1이상 1000이하
시험관의 정보 n개. 그래프이다.
s, x, y 제시. s초 후에, x,y행은 무엇인지.
'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
s, x, y = map(int, input().rstrip().split())
q = deque() # point list
pl = []
for i in range(n):
    for j in range(n):
        if g[i][j] != 0:
            pl.append((g[i][j], (i, j, 0))) # 값, (좌, 표, 카운트)
pl.sort() # 작은 순서대로 해야함
while pl:
    q.append(pl.pop(0)[1]) # 좌표랑 카운트만 넣어준다.

# 사방이동
dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]
# bfs 실행
while q:
    h, w, c = q.popleft()
    for i in range(4):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<n and g[nh][nw] == 0 and c+1<=s:
            g[nh][nw] = g[h][w]
            if nh == x-1 and nw == y-1:
                break
            q.append((nh, nw, c+1))

print(g[x-1][y-1])



