'''
빵집

가스관을 훔칠 것.
빵집은 R*C. 첫째 열은 빵집 근처, 마지막 열은 원웅이네.
가스관과 빵집을 연결하는 모든 파이프 라인은 첫째 열에서 시작해야하고, 마지막 열에서 끝나야 한다.
각 칸은 오른쪽, 오른쪽 위 대각선, 오른쪽 ㅏㅇ래 대각선으로 연결 할 수 있고, 각 칸의 중심끼리 연결하는 것이다. 가스 많이 훔칠거다. 각 칸을 지나는 파이프는 하나여야 한다.
빵집 제시되었을 때, 파이프라인 최대 갯수

입력
n, m  제시.
n개 줄 그래프 제시. 처음과 마지막 열은 항상 비어있다.

출력
파이프라인 최대 갯수
'''
import sys
input = sys.stdin.readline

mov = [(-1,1), (0,1), (1,1)] # 위에서부터 탐색하면 항상 위쪽 먼저, 아래는 아래 먼저
# 의문을 가졌던 대각으로 겹치는 경우가 생기면 어떡하지? 라는 내용은 그렇게 나올 수가 없는듯. 우하단 내려가는 것은 우측/우상단 벽 혹은 방문 상태인건데 그러면 우상단으로 겹쳐갈 수 없음.
# 또한 애초에 아래 파이프는 위 파이프보다 위쪽으로 갈 수가 없음 대각 위로 넘어가려고 해도 벽 아니면 위쪽이 먼저 탐색하기 때문에.

def dfs(h, w):
    global n, m, fla, dep, ans
    if w==m-1:
        dep = h
        ans += 1
        fla = True
    if fla:
        return
    for dh, dw in mov:
        nh, nw = h+dh, w+dw
        if 0<=nh<n and 0<=nw<m and g[nh][nw] == '.' and not v[nh][nw]:
            v[nh][nw] = 1
            dfs(nh, nw)
            if fla:
                return

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
v = [[0]*m for _ in range(n)]
ans = 0
for i in range(n):
    fla = False
    dep = -1
    v[i][0] = 1
    dfs(i, 0)
    if dep == n-1:
        break

print(ans)


