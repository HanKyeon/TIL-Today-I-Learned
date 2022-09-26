'''
사다리 조작

사다리 게임은 n개의 세로선과 m개의 가로선으로 이루어져 있다.
세로선 사이에는 가로선을 둘 수 있다. 각 세로선마다 가로선을 놓을 수 있는 위치 갯수는 h이다.
가로선은 인접한 두 세로선을 연결한다. 두 가로선이 연속하거나 겹쳐서는 안된다.
사다리에 가로선을 추가해서, 사다리 게임의 결과를 조작하려고 한다. 이때, i번 세로선의 결과가 i번이 나와야 한다. 그렇게 하기 위해서 추가해야 하는 가로선 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
세러선 갯수n, 가로선 갯수m, 세로선마다 가로선 놓을 수 있는 위치 갯수 h 제시.
m개 줄에 가로선 정보 a, b 제시. b번 세로선과 b+1 세로선을 a번 점선 위치에서 연결.
가장 위의 점선 번호는 1, 아래로 내려갈 때마다 1 증가.
세로선은 가장 왼쪽이 1, 증가. 가로선이 서로 연속하는 경우 x

출력
i번 세로선의 결과가 i번이 나오도록 게임을 조작해야 한다.
정답이 3 이상, 혹은 불가능일 경우 -1 출력.
'''
from itertools import combinations
import sys
input = sys.stdin.readline

def ladder():
    global n, k, garo
    for i in range(1, n+1):
        h, w = 1, i
        while h <= k:
            if garo.get((h, w), 0):
                h, w = garo[(h, w)]
            h+=1
        if w != i:
            return False
    return True

n, m, k = map(int, input().rstrip().split())
garos = {}
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    garos[(a, b)] = (a, b+1)
    garos[(a, b+1)] = (a, b)
able=[]
for i in range(1, n):
    for j in range(1, k+1):
        if garos.get((j, i), 0):
            continue
        if garos.get((j, i+1), 0):
            continue
        able.append((j, i))

ans = -1
for i in range(4):
    for j in combinations(able, i):
        garo = {k:v for k, v in zip(garos.keys(), garos.values())}
        for kk in range(i):
            garo[(j[kk][0], j[kk][1])] = (j[kk][0], j[kk][1]+1)
            garo[(j[kk][0], j[kk][1]+1)] = (j[kk][0], j[kk][1])
        a = ladder()
        if a:
            ans = i
            break
    if ans >= 0:
        break
print(ans)

'''
더 빠른 코드

import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
graph = [[0]*N for _ in range(H)]
for i in range(1, M+1):
    a, b = map(int, input().split())
    graph[a-1][b-1] = i
    graph[a-1][b] = i

def isBridgeLeft(y, x): # 왼쪽에 다리가 있는가?
    return True if x-1 >= 0 and graph[y][x-1] == graph[y][x] else False

def isBridgeRight(y, x): # 오른쪽에 다리가 있는가?
    return True if x+1 < N and graph[y][x+1] == graph[y][x] else False

def simulation():  # 사다리게임 시뮬레이션 ..
    for i in range(N):
        cury, curx = 0, i
        while cury < H:
            if graph[cury][curx] != 0: # 다리가 있다.
                if isBridgeLeft(cury, curx): # 왼쪽에 다리가 있다면
                    curx -= 1
                elif isBridgeRight(cury, curx): # 오른쪽에 다리가 있다면
                    curx += 1
            cury += 1

        if curx != i:
            return False
    return True

def dfs(start, c):
    global answer
    if c == cnt+1:
        if simulation():
            answer = c
        return

    for i in range(start, N*H):
        y, x = i//N, i%N
        if x == N-1:
            continue
        if graph[y][x] == 0 and isBridgeRight(y, x):
            graph[y][x] = M+c
            graph[y][x+1] = M+c
            dfs(i+1, c+1)
            graph[y][x] = 0
            graph[y][x+1] = 0

answer = -1
for cnt in range(4):
    dfs(0, 1)
    if answer != -1:
        break


if answer != -1:
    answer -= 1
print(answer)
'''

'''
빠른 코드

N, M, H = map(int, input().split())
ans = 0
ladder = [[0 for _ in range(N)] for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = 2

def check():
    for i in range(N):
        tmp = i
        for j in range(H):
            if ladder[j][i] == 2:
                i -= 1
            elif ladder[j][i] == 1:
                i += 1

        if tmp != i:
            return False
    return True

line_num = 0

def dfs(d, idx):
    if line_num == d:
        if check():
            return True
    else:
        for ii in range(idx, (N-1)*H):
            i = ii // (N-1)
            j = ii % (N-1)
            if ladder[i][j+1] == 0 and\
                ladder[i][j] == 0:
                ladder[i][j] = 1
                ladder[i][j+1] = 2
                if dfs(d+1, ii):
                    return True
                ladder[i][j+1] = 0
                ladder[i][j] = 0
        return False

for i in range(4):
    line_num = i
    if dfs(0, 0):
        print(i)
        break
else:
    print(-1)
'''







