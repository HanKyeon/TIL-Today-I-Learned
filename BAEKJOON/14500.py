'''
테트로미노

폴리오미노란 1*1 정사각형 붙인 도형이며 조건 만족해야한다.

정사각형 겹치면 x
도형은 모두 연결.
정사각형 변 끼리 연결되어 있어야 한다.
정사각형 4개를 이어 붙인 폴리오미노는 테트로미노. 5가지 존재. 직선 ㄴ 네모 지그재그 ㅗ.
N M 종이 위에 테트로미노 하나를 놓았을 때 최댓값은?
테트로미노 회전 대칭 가능.

입력
N, M 제시. 4이상 500이하.
종이에 쓰여있는 수 제시.

출력
최댓값
'''

'''
- 가장 큰 값의 절반부터 해서 봐보자.
아이디어

두칸의 합 이후 주변 6칸 중 택2 해서 계산.
두칸은 가로 두줄, 세로 두 줄. 윗칸 아랫칸 / 왼쪽칸 오른쪽칸 크게 둘로 나누고
각 칸에 대해서 3개 중 택1 하여 계산해보는 방식.

가로 dgh dgw 세로 dsh dsw 이렇게 탐색 영역을 줄이고
x, y를 인자로 받아서 x2y2를 만들어서 탐색
우하단에서 어느 인덱스까지 할 지 고민할듯.

아이디어2
각 칸에 대해 dfs를 하여 세트에 넣고, 세트를 훑으며 합을 구해줌. -> ㅗ ㅜ 가 안됨.
혹은 x,y에 대하여 세트에 한 칸을 dfs 했을 때 나올 수 있는 가능성을 다 구해놓고 각 칸에 대해 검증만 해도 될듯?
'''
'''
from itertools import combinations
import sys
input = sys.stdin.readline

def ms(h1, w1):
    global sets
    global m, n

    h2, w2 = h1 + 1, w1
    if 0<=h2<n and 0<= w2 < m:
        ml = [(h1, w1), (h2, w2)]
        ps = [(h1-1, w1), (h1, w1-1), (h1, w1+1), (h2+1, w2), (h2, w2-1), (h2, w2+1)]
        for i in combinations(ps, 2):
            i = list(i)
            if 0 <= i[0][0] < n and 0 <= i[0][1] < m and 0 <= i[1][0]< n and 0 <= i[1][1] < m:
                sets.add(tuple(ml+i))

    h2, w2 = h1, w1 + 1
    if 0<=h2<n and 0<= w2 < m:
        ml = [(h1, w1), (h2, w2)]
        ps = [(h1, w1-1), (h1+1, w1), (h1-1, w1), (h2, w2+1), (h2+1, w2), (h2-1, w2)]
        for i in combinations(ps, 2):
            i = list(i)
            if 0 <= i[0][0]< n and 0 <= i[0][1] < m and 0 <= i[1][0]< n and 0 <= i[1][1] < m:
                sets.add(tuple(ml+i))

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
sets = set()
mnv = max(map(max, g))//4+1
cm = 0
for i in range(n):
    for j in range(m):
        ms(i, j)
while sets:
    a, b, c, d = sets.pop()
    cm = max(g[a[0]][a[1]] + g[b[0]][b[1]] + g[c[0]][c[1]] + g[d[0]][d[1]], cm)
print(cm)
'''

from itertools import combinations
import sys
input = sys.stdin.readline

def ms(h1, w1):
    global sets
    global m, n
    pz = set()
    h2, w2 = h1 + 1, w1
    if 0<=h2<n and 0<= w2 < m:
        ml = [(h1, w1), (h2, w2)]
        ps = [(h1-1, w1), (h1, w1-1), (h1, w1+1), (h2+1, w2), (h2, w2-1), (h2, w2+1)]
        for i in combinations(ps, 2):
            i = list(i)
            if 0 <= i[0][0] < n and 0 <= i[0][1] < m and 0 <= i[1][0]< n and 0 <= i[1][1] < m:
                pz.add(tuple(ml+i))

    h2, w2 = h1, w1 + 1
    if 0<=h2<n and 0<= w2 < m:
        ml = [(h1, w1), (h2, w2)]
        ps = [(h1, w1-1), (h1+1, w1), (h1-1, w1), (h2, w2+1), (h2+1, w2), (h2-1, w2)]
        for i in combinations(ps, 2):
            i = list(i)
            if 0 <= i[0][0]< n and 0 <= i[0][1] < m and 0 <= i[1][0]< n and 0 <= i[1][1] < m:
                pz.add(tuple(ml+i))

    ret = 0
    while pz:
        a, b, c, d = pz.pop()
        ret = max(g[a[0]][a[1]] + g[b[0]][b[1]] + g[c[0]][c[1]] + g[d[0]][d[1]], ret)
    return ret

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
sets = set()
cm = 0
for i in range(n):
    for j in range(m):
        cm = max(ms(i, j), cm)
print(cm)

'''
# 짱 빠른 코드. 이게 백 트래킹이라 이말이야! 같다.
import sys; input = sys.stdin.readline

def dfs(x, y, step, total):
    global answer
    # 종료조건1) 탐색을 계속 진행하여도 최댓값에 못 미치는 경우
    if total + max_val*(4-step) <= answer:
        return

    # 종료조건2) 블록 4개를 모두 활용한 경우
    if step == 4:
        answer = max(answer, total)
        return

    # 상하좌우 방향으로 블록 이어 붙여 나가기
    for dx, dy in d:
        nx = x + dx # 새로운 x 좌표
        ny = y + dy # 새로운 y 좌표
        # 새로운 좌표가 유효한 범위 내 있고 탐색이력이 없는 경우
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            # 2번째 블록 연결 후 'ㅏ','ㅓ','ㅗ','ㅜ' 만들기
            if step == 2:
                visited[nx][ny] = True # 탐색기록
                # 새로운 좌표에서 탐색하지 않고 기존 좌표로 돌아와 탐색재개
                dfs(x, y, step+1, total+board[nx][ny])
                visited[nx][ny] = False # 탐색기록 제거

            visited[nx][ny] = True
            dfs(nx, ny, step+1, total+board[nx][ny])
            visited[nx][ny] = False

if __name__ == "__main__":
    N, M = map(int, input().split()) # 좌표의 행, 열 개수
    board = [list(map(int, input().split())) for _ in range(N)] # 좌표별 값
    max_val = max(map(max, board)) # 모든 좌표 중 최댓값
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 좌표 내 상하좌우
    visited = [[False] * M for _ in range(N)] # 탐색여부 확인용
    answer = 0

    for i in range(N):
        for j in range(M):
            visited[i][j] = True # 탐색기록
            dfs(i, j, 1, board[i][j])
            visited[i][j] = False # 탐색기록 제거
    print(answer)
'''











