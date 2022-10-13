'''
스티커 붙이기

스티커 받았다. 스티커를 무조건 좌상단부터 채워나간다. 또한 스티커는 연결되어 있어야 한다.
스티커를 붙이는 방법은 다음과 같다.
1. 회전시키지 않고 모눈종이에서 떼어낸다.
2. 다른 스티커와 겹치거나 노트북을 벗어나지 않으면서 스티커를 붙일 수 있는 위치를 찾는다. 위쪽부터 채워나가고 왼쪽부터 채워나갈 것이다.
3. 선택한 위치에 스티커를 붙인다. 위치가 없어서 붙이지 못했다면 90도 회전해서 반복.
4. 0, 90, 180, 270 회전 시켜도 못붙이면 버린다.

입력
세로 가로 스티커 갯수 n, m, k 제시.
k개 스티커 정보 제시.
r, c 제시
모양 제시. 1은 스티커 0은 노스티커

출력
스티커를 붙였을 때, 노트북에서 스티커가 붙은 칸의 수 출력.
'''
import sys
input = sys.stdin.readline

def check(h, w):
    global n, m, r, c, ans
    fla = False
    nl = []
    for i in range(h, h+r):
        for j in range(w, w+c):
            if g[i][j] * stk[i-h][j-w]:
                return fla
            if stk[i-h][j-w]:
                nl.append((i, j))
    fla = True
    for h, w in nl:
        g[h][w] = 1
        ans += 1
    return fla

def lego():
    global n, m, r, c
    fla = False
    for i in range(n-r+1):
        for j in range(m-c+1):
            fla = check(i, j)
            if fla:
                return fla
    return fla

def turn90():
    global r, c, stk
    nstk = [[] for _ in range(c)]
    for i in range(c):
        for j in range(r-1, -1, -1):
            nstk[i].append(stk[j][i])
    stk = []
    for i in nstk:
        stk.append(i[:])
    r, c = c, r

n, m, k = map(int, input().rstrip().split())
g = [[0]*m for _ in range(n)]
ans = 0
for _ in range(k):
    r, c = map(int, input().rstrip().split())
    stk = [list(map(int, input().rstrip().split())) for _ in range(r)]
    if lego():
        continue
    turn90()
    if lego():
        continue
    turn90()
    if lego():
        continue
    turn90()
    if lego():
        continue

print(ans)










