'''
혁진이의 프로그램 검증
기본적으로 좌상단에서 우측으로 출발
<	이동 방향을 왼쪽으로 바꾼다.
>	이동 방향을 오른쪽으로 바꾼다.
^	이동 방향을 위쪽으로 바꾼다.
v	이동 방향을 아래쪽으로 바꾼다.
_	메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
|	메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다. 방향이 바뀔 확률은 네 방향 동일하다.
.	아무 것도 하지 않는다.
@	프로그램의 실행을 정지한다.
0~9	메모리에 문자가 나타내는 값을 저장한다.
+	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다.
-	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다.
프로그램 정지가 가능한지 아닌지 판단.

입력
테케 T
2이상 20이하 R, C. R행 C열
R개 줄 각각 C개 문자

출력
#T 정지가능YES 정지 불가능 NO
'''

import sys
sys.stdin = open("input.txt", "r")

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
def 함수(g, mem, h, w, d):
    global n, m, f
    global sets
    if f != None:
        return f
    if h < 0:
        h = n-1
    elif h >= n:
        h = 0
    if w < 0:
        w = m-1
    elif w >= m:
        w = 0

    if g[h][w] == '@':
        f = True
        return True
    if (mem, h, w, d) in sets:
        f = False
        return False
    sets.add((mem, h, w, d))
    nh, nw = h+dh[d], w + dw[d]
    if g[h][w] == '>':
        d = 3
        nh, nw = h + dh[d], w + dw[d]
        return 함수(g, mem, nh, nw, d)
    elif g[h][w] == '<':
        d = 2
        nh, nw = h + dh[d], w + dw[d]
        return 함수(g, mem, nh, nw, d)
    elif g[h][w] == '^':
        d = 0
        nh, nw = h + dh[d], w + dw[d]
        return 함수(g, mem, nh, nw, d)
    elif g[h][w] == 'v':
        d = 1
        nh, nw = h + dh[d], w + dw[d]
        return 함수(g, mem, nh, nw, d)
    elif g[h][w] == '_':
        if mem == 0:
            d = 3
        elif mem != 0 :
            d = 2
        nh, nw = h + dh[d], w + dw[d]
        return 함수(g, mem, nh, nw, d)
    elif g[h][w] == '|':
        if mem == 0:
            d = 1
        elif mem != 0 :
            d = 0
        nh, nw = h + dh[d], w + dw[d]
        return 함수(g, mem, nh, nw, d)

    elif g[h][w] == '?':
        return 함수(g, mem, h+dh[0], w+dw[0], 0) or 함수(g, mem, h+dh[1], w+dw[1], 1) or 함수(g, mem, h+dh[2], w+dw[2], 2) or 함수(g, mem, h+dh[3], w+dw[3], 3)

    elif g[h][w] == '.':
        return 함수(g, mem, nh, nw, d)
    elif g[h][w] == '+':
        mem += 1
        if mem > 15:
            mem = 0
        return 함수(g, mem, nh, nw, d)
    elif g[h][w] == '-':
        mem -= 1
        if mem < 0:
            mem = 15
        return 함수(g, mem, nh, nw, d)
    elif g[h][w] in list(map(str, range(10))):
        mem = int(g[h][w])
        return 함수(g, mem, nh, nw, d)

for testcase in range(1, int(input())+1):
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    h, w, mem, d = 0, 0, 0, 3
    sets = set()
    alp = []
    f = None
    for i in g:
        if '@' in i:
            alp.append(True)
    if alp == []:
        print(f"#{testcase} NO")
    else:
        a = 함수(g, 0, h, w, d)
        if a == True:
            a = 'YES'
        elif a == False:
            a = 'NO'
        print(f"#{testcase} {a}")




3 28 29 30 45 52 54 59 62 69


