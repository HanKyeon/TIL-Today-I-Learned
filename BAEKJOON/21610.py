'''
마법사 상어와 비바라기

n*n 격자. a[r][c]는 r행c열 바구니에 저장된 물의 양.
격자 좌상당 1,1 우하단 n,n. 1번행과 n번 행을 연결, 1번 열과 n번 열도 연결.
비바라기를 시전하면 n,1 / n,2 / n-1,1 / n-1,2 에 비구름이 생긴다. 구름은 칸 전체 차지.
구름에 이동을 m번 명령. i번째 이동 명령은 방향d와 거리s로 이루어져 있다. 8방향, 8정수 표시.
1좌 2좌상 3상 4우상 5우 6우하 7하 8좌하

이동 명령 시 행동
1. 모든 구름이 di 방향으로 si칸 이동.
2. 비가 내려서 저장된 물의 양이 1 증가.
3. 구름 삭제
4. 물이 증가한 칸에 물 복사 마법. 물 복사 시 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수 만큼 r,c에 있는 바구니의 물의 양이 증가.
4-1. 이 때 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다. 예를 들어 n,2 인접 대각선은 n-1,1 n-1,3이고 n,n에서 인접한 대각선 칸은 n-1, n-1 뿐이다.
5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이 때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.

m번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합.

입력
n, m 제시.
그래프 제시.
m개 줄
이동 정보 제시. di, si. di는 1 빼서 쓰자.
'''
from collections import deque
import sys
input = sys.stdin.readline

def clmove(di, s):
    nq = deque() # 이동한 구름 장소
    savc = set() # 이번에 비내리는 장소
    # 구름 이동
    while q:
        h, w = q.popleft()
        h, w = (h+dh[di]*s) % n, (w+dw[di]*s) % n
        nq.append((h, w))
    # 비내리기
    while nq:
        h, w = nq.popleft()
        g[h][w] += 1
        savc.add((h, w))
    # 물복사
    for h, w in savc:
        for i in (1,3,5,7):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<n and g[nh][nw]:
                g[h][w] += 1
    # 구름 띄우기
    for i in range(n):
        for j in range(n):
            if g[i][j] < 2:
                continue
            if (i, j) in savc:
                continue
            g[i][j] -= 2
            q.append((i, j))

# 대각선은 1 3 5 7
dh = [0, -1, -1, -1, 0, 1, 1, 1]
dw = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
q = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]) # 첫 비구름
for _ in range(m):
    di, si = map(int, input().rstrip().split())
    clmove(di-1, si)
print(sum(map(sum, g)))






'''
    for i in range(n):
        for j in range(n):
            if cld[i][j]:
                h, w = (i+dh[di]*s) % n, (j+dw[di]*s) % n
                q.append((h, w, cld[i][j]))
                cld[i][j] = 0
'''






