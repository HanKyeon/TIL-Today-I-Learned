'''
연구소

연구소에 바이러스 유출. 연구소에 벽 세울 것.
연구소는 N*M 직사각형으로 표현. 직사각형은 1*1 정사각형으로 나눠져 있음.
연구소는 빈칸/벽으로 구성, 벽은 칸 하나를 가득 차지.
일부 칸은 바이러스가 존재. 상하좌우 인전한 빈 칸으로 모두 퍼져나간다.
세울 수 있는 벽의 갯수는 3개, 꼭 3개를 세워야 한다.

입력
지도의 세로크기 N, 가로크기 M 제시 N, m은 3이상 8이하
N개의 줄이 지도에 배치.
0은 빈 칸, 1은 벽, 2는 바이러스.
2의 갯수는 2보다 크거나 같고 10보다 작거나 같은 자연수. 빈칸은 3개 이상.

출력
안전 영역의 최대 크기
'''
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
# 바이러스 퍼트리고 남은 0의 갯수 세서 리턴
dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]

def bfs(vli, v):
    global n, m, zc
    q = deque()
    for i in vli:
        q.append(i)

    while q:
        h, w = q.pop()
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<m and v[nh][nw] == 0 and g[nh][nw] == '0':
                v[nh][nw] = 1
                zc += 1
                q.append((nh, nw))
    return zc

n, m = map(int, input().split())
g = [list(input().split()) for _ in range(n)]
vrs, zrs = [], []
# 순회하며 바이러스와 0좌표 찾기
for i in range(n):
    for j in range(m):
        if g[i][j] == '2':
            vrs.append((i,j))
        elif g[i][j] == '0':
            zrs.append((i,j))
# 콤비네이션으로 점 3개 뽑기
wls = list(combinations(zrs, 3))
anl = [] # 점 3개마다 센 감염된 0의 갯수
# 실행
for i in wls: # 3개의 조합 점들을 보고
    a, b, c = i # 배분
    zc = 0 # 감염되는 0 갯수
    v = [[0]*m for _ in range(n)] # 방문
    g[a[0]][a[1]], g[b[0]][b[1]], g[c[0]][c[1]] = '1', '1', '1' # 기둥처리
    anl.append(bfs(vrs, v)) # bfs하면서 감염한 0 갯수 담기
    g[a[0]][a[1]], g[b[0]][b[1]], g[c[0]][c[1]] = '0', '0', '0' # 기둥 폐기

print(len(zrs)-min(anl)-3)
