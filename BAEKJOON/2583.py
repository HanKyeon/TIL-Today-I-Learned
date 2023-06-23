'''
영역 구하기

m*n 크기 모눈종이. k개의 정사각형 그릴 때 k개 직사각형 내부를 제외한 나머지 부분이 몇개의 분리된 영역으로 나뉜다.
m n k 랑 k개 직사각형 좌표 제시. 몇개의 분리 영역으로 나뉘는지, 각 영역 넓이 구해라.

입력
m, n, k 제시. 100이하 자연수
k개 줄 좌하단 우상단 x, y좌표 제시. 좌하단 0,0 우상한 n,m

출력
나눠지는 영역 갯수
넓이를 오름차순 정렬 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

def coloring(h1, w1, h2, w2):
    for i in range(h1, h2):
        for j in range(w1, w2):
            g[i][j] = 1

def bfs(h, w):
    q = deque([(h, w)])
    g[h][w] = 1
    ret= 1
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and not g[nh][nw]:
                g[nh][nw] = 1
                ret+=1
                q.append((nh, nw))
    return ret

mov = [(-1,0),(0,1),(1,0),(0,-1)]
m, n, k = map(int, input().rstrip().split())
g = [[0]*m for _ in range(n)]
for _ in range(k):
    h1, w1, h2, w2 = map(int, input().rstrip().split())
    coloring(h1, w1, h2, w2)
ans = []
for i in range(n):
    for j in range(m):
        if g[i][j]:
            continue
        ans.append(bfs(i, j))
ans.sort()
print(len(ans))
print(*ans)
