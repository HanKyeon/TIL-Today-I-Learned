'''
달이 차오른다, 가자.

민식이는 미로 속에 있다. 직사각형, 미로 탈출.

. : 빈 칸
# : 벽. 이동 불가
a,b,c... : 열쇠. 언제나 이동 가능.
A,B,C : 문. 해당 열쇠가 있어야 이동 가능.
0 : 민식이 현재 위치. 빈 곳이고, 민식이가 현재 서 있는 곳
1 : 출구

사방이동 1회판정일 때, 미로 탈출하는데 걸리는 이동 횟수의 최솟값 계산.

입력
n, m 제시.
0은 한 개, 1은 적어도 한 개

출력
민식이가 미로를 탈출하는데 드는 이동 횟수의 최솟값 출력. 탈출 불가능 시 -1 출력
'''
# 열쇠는 a b c d e f 7종류
# 문도 A B C D E F 7종류
from collections import deque
import sys
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs():
    while q:
        h, w, ks, cnt = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0 <= nh < n and 0 <= nw < m and s[nh][nw] != "#" and v[nh][nw][ks] == 0:
                if s[nh][nw] == ".":
                    v[nh][nw][ks] = 1
                    q.append([nh, nw, ks, cnt + 1])
                elif s[nh][nw] == "1":
                    return cnt+1
                else:
                    if s[nh][nw].isupper():
                        if ks & 1 << (ord(s[nh][nw]) - 65):
                            v[nh][nw][ks] = 1
                            q.append([nh, nw, ks, cnt + 1])
                    elif s[nh][nw].islower():
                        nc = ks | (1 << ord(s[nh][nw]) - 97)
                        if v[nh][nw][nc] == 0:
                            v[nh][nw][nc] = 1
                            q.append([nh, nw, nc, cnt + 1])
    return -1
n, m = map(int, input().rstrip().split())
s = []
q = deque()
v = [[[0] * 64 for _ in range(m)] for _ in range(n)]
for i in range(n):
    a = list(input().rstrip())
    s.append(a)
    for j in range(m):
        if a[j] == "0":
            q.append([i, j, 0, 0])
            s[i][j] = "."
            v[i][j][0] = 1
print(bfs())

'''
a키만 갖고있을때 - 000001
b키만 갖고 있을때 - 000010
a, b 둘다 갖고 있을때 - 000011
이런식으로 이진법으로 변환하여 나타낼 수 있다.
가지수는 64가지이고 3차원 배열을 만들어 주어서 visit을 체크 해준다.
'''












'''
# 시간초과와 메모리 초과.

from collections import deque
import sys
input = sys.stdin.readline

smz, dmz = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mov = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs():
    global n, m
    di = {'':[[0]*m for _ in range(n)]}
    q = deque()
    while ms:
        h, w = ms.pop()
        di[''][h][w] = 1
        q.append((h, w, '', 0))
    while q:
        h, w, nks, cnt = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == 0 and not di[nks][nh][nw]:
                di[nks][nh][nw] = 1
                q.append((nh, nw, nks, cnt+1))
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] == 0 and di[nks][nh][nw]:
                continue
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] == 1:
                continue
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] == 2:
                return cnt+1
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] in smz and g[nh][nw] not in nks:
                di[nks+g[nh][nw]] = [[0]*m for _ in range(n)]
                di[nks+g[nh][nw]][nh][nw] = 1
                q.append((nh, nw, nks+g[nh][nw], cnt+1))
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] in smz and g[nh][nw] in nks:
                di[nks][nh][nw] = 1
                q.append((nh, nw, nks, cnt+1))
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] in dmz and not di[nks][nh][nw]:
                if chr(ord(g[nh][nw])+32) in nks:
                    di[nks][nh][nw] = 1
                    q.append((nh, nw, nks, cnt+1))
    # for i in di:
    #     print(i)
    #     for j in di[i]:
    #         print(j)
    #     print('=====')
    return -1

# 대문자A 65
# 소문자a 97
# 차이는 32

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
ms = []
# 통과 가능 0, 벽 1, 목적지 2, 문 65~~, 열쇠 97~~
for i in range(n):
    for j in range(m):
        if g[i][j] == '0':
            ms.append((i, j))
            g[i][j] = 0
        elif g[i][j] == '.':
            g[i][j] = 0
        elif g[i][j] == '#':
            g[i][j] = 1
        elif g[i][j] == '1':
            g[i][j] = 2
# for i in g:
#     print(i)
print(bfs())
'''










