'''
주사위 굴리기2

크기가 n*m 지도.
주사위는 최초 2 / 4 1 3 / 5 / 6 상태.
처음 주사위의 이동 방향은 동쪽.

이동 방법
1. 주사위가 이동 방향으로 한 칸 굴러간다. 만약 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
2. 주사위가 도착한 칸 x,y에 대한 점수 획득.
3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 x, y에 있는 정수 B를 비교해 이동 방향을 결정한다.
3-1. A>B 인 경우, 90도 시계방향 회전, A<B인 경우 90도 반시계, A==B continue

칸 x,y에 대한 점수 구하기.
x, y에 있는 숫자 B. 동서남북 방향으로 연속해서 이동 할 수 있는 칸의 수(bfs로 연속되게 있는 갯수들. dp로 해두면 편할 것 같다.) C를 모두 구한다. 이 때, 이동 할 수 있는 칸에는 모두 정수 B가 있어야 한다. 점수는 C와 B를 곱한 값.

보드의 크기와 각 칸에 있는 정수, 주사위의 이동 횟수K가 주어졌을 때, 각 이동에서 획득하는 점수의 합을 구해보자.

입력
n, m , k 제시.
그래프 제시.

출력
획득 점수의 합 출력
'''
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

zsw = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6}
def zg(di):
    if di == 0:
        zsw[1], zsw[2], zsw[5], zsw[6] = zsw[5], zsw[1], zsw[6], zsw[2]
    if di == 1: # correct
        zsw[1], zsw[3], zsw[4], zsw[6] = zsw[4], zsw[1], zsw[6], zsw[3]
    if di == 2:
        zsw[1], zsw[2], zsw[5], zsw[6] = zsw[2], zsw[6], zsw[1], zsw[5]
    if di == 3:
        zsw[1], zsw[3], zsw[4], zsw[6] = zsw[3], zsw[6], zsw[1], zsw[4]

def dfs(h, w):
    global n, m, cnt
    for i in range(4):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<m and g[nh][nw] == g[h][w] and not v[nh][nw]:
            cnt+=1
            v[nh][nw] = 1
            dfs(nh, nw)
    v[h][w] = cnt

n, m, k = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if v[i][j]:
            continue
        cnt = 1
        v[i][j] = 1
        dfs(i, j)

h, w, di = 0, 0, 1
ans = 0
while k:
    k-=1
    # print(di)
    nh, nw = h+dh[di], w+dw[di]
    if 0<=nh<n and 0<=nw<m:
        h, w = nh, nw
        zg(di)
        # print(di, '안쪽')
        if zsw[6] > g[h][w]:
            di = (di+1)%4
        elif zsw[6] < g[h][w]:
            di = (di+3)%4
    else:
        di = (di+2)%4
        nh, nw = h+dh[di], w+dw[di]
        zg(di)
        # print(di, '벗어남')
        h, w = nh, nw
        if zsw[6] > g[h][w]:
            di = (di+1)%4
        elif zsw[6] < g[h][w]:
            di = (di+3)%4
    ans += v[h][w] * g[h][w]
    # print(g[h][w], zsw, h, w, ans)
print(ans)






'''
1231211
'''




