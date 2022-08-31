'''
탈출

비어있는 곳 . 물 * 돌 X 비버굴D 고슴도치S
고슴도치는 인접한 네 칸 중 하나로 이동 가능. 물도 매 분 비어있는 칸으로 확장.
물과 도치는 돌 패스 못함. 도치는 물이 찰 예정인 구역도 못간다. 물은 비버 소굴로 이동 못한다.

- 도치가 가고 물이 지우면 상관 없다.

입력
50이하 자연수 R과 C 제시.
R개 줄에 티떱숲 지도 제시. D와 S는 pk이다.

출력
도치가 비버굴로 이동 할 수 있는 가장 빠른 시간 출력. 이동 못함녀 KAKTUS 출력
'''
from collections import deque
import sys
input = sys.stdin.readline
# 사방이동
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

r, c = map(int, input().rstrip().split()) # row column
g = [list(input().rstrip()) for _ in range(r)] # 그래프
wat, had = [], [] # 물 좌표 비버집 고슴도치
for i in range(r):
    for j in range(c):
        if g[i][j] == '*': wat.append((i, j)) # 물좌표
        elif g[i][j] == 'S': had.append((i, j, 0)) # 고슴도치 좌표

q = deque() # 큐
for i in had:
    q.append(i) # 고슴도치 먼저
for i in wat:
    q.append(i) # 물 넣기
ans = 0
while q:
    # print('==============')
    # for i in g:
    #     print(*i)
    # print('==============')
    info = q.popleft() # 일단 빼서
    if len(info) == 2: # 길이 2면 물
        h, w = info
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<r and 0<=nw<c and (g[nh][nw] == '.' or g[nh][nw] == 'S'): # 물이나 고슴도치면 침수시킴
                g[nh][nw] = '*'
                q.append((nh, nw))
    elif len(info) == 3: # 길이 3이면 고슴도치
        h, w, cn = info
        if g[h][w] == '*': # 침수 당했으면 확인 안함
            continue
        else:
            for i in range(4):
                nh, nw = h+dh[i], w+dw[i]
                if 0<=nh<r and 0<=nw<c and g[nh][nw] == '.': # 그냥 이동 가능하면 이동 시키고
                    g[nh][nw] = 'S'
                    q.append((nh, nw, cn+1))
                elif 0<=nh<r and 0<=nw<c and g[nh][nw] == 'D': # 비버네면 정답 넣고 그만
                    ans = cn+1
                    break
            if ans: # 정답 들어갔으면 끝
                break

if not ans: # 다 했는데 정답 안들어가면
    ans = 'KAKTUS' # 캌투스
print(ans) # 출력




