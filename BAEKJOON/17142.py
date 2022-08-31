'''
연구소3

상하좌우 동시복제, 1초. M개를 활성 상태로 할 것.
n*n 연구실. 빈 칸0 벽1 바이러스2. 바이러스가 바이러스 터치하면 바이러스됨
- 바이러스 만나면 숫자 그대로 감염 시키면 될듯?

입력
n 4이상 50이하, m1이상 10이하
그래프. 0은 빈 칸 1은 벽 2는 바이러스 2의 갯수는 m이상 10이하

출력
모든 빈 칸에 바이러스가 있게 되는 최소 시간 출력. 불가능 시 -1 출력
'''
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
# 사방이동
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
'''
n, m = map(int, input().rstrip().split()) # 크기, 가능 갯수
g = [list(map(int, input().rstrip().split())) for _ in range(n)] # 그래프g
vst = [] # 바이러스 시작 지점
wiz = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == 2:
            vst.append((i, j))
        if g[i][j] == 0:
            wiz+=1
if wiz == 0: # 0 없으면 0초
    print(0)
else:
    ans = int(10e9) # 답
    for vir in combinations(vst, m): # 조합
        v = [] # 그래프 복사해서 받아 방문처리 할 것
        for i in g:
            v.append(i[:])
        si = set(vir) # 시작점은 bfs에 들어갈 이유 없으나 다른 2는 훑어봐야 하기 때문에 방문처리 따로 관리
        q = deque(vir) # 큐
        fla = True # 갱신 여부 확인
        while q:
            h, w = q.popleft()
            # print(h, w)
            a = v[h][w]+1 # 카운트
            for i in range(4): # 사방탐색
                nh, nw = h + dh[i], w + dw[i]
                if 0<=nh<n and 0<=nw<n and v[nh][nw] == 0:
                    v[nh][nw] = a
                    q.append((nh, nw))
                elif 0<=nh<n and 0<=nw<n and (v[nh][nw] == 2 and not (nh, nw) in si):
                    v[nh][nw] = a
                    q.append((nh, nw))
        if fla: # 0이 있으면 갱신 안할거다.
            for i in v:
                if 0 in i:
                    fla = False
                    break
        if fla: # 그거 아니면 갱신할거임~
            c = 0
            for i in range(n):
                for j in range(n):
                    if (i, j) in vst:
                        continue
                    if v[i][j] > c:
                        c = v[i][j]
            ans = min(ans, c)
            # print('======')
            # for i in v:
            #     print(*i)
            # print('======')

    if ans != int(10e9): # 갱신이 되었으면 시작값이 2이므로 2 빼서 출력
        print(ans-2)
    else: # 끝까지 갱신 안됐다면 0이 무조건 있는 것이므로 -1
        print(-1)
'''



'''
# 시간 초과

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def bfs2(ph,pw): # 2가 있는 지점마다 확인할 것. 주변에 뻗어나갈 수 있다면 True 반환, 아니라면 False 반환
    global n, v
    q = deque()
    sets = set() # 방문처리를 set로 할 것. 어차피 인접한 2들로만 뻗어가는 bfs이므로.
    q.append((ph,pw))
    sets.add((ph, pw))
    while q:
        h, w = q.popleft()
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<n and v[nh][nw] == 0: # 뻗어나갈 수 있으면 True
                return True
            elif 0<=nh<n and 0<=nw<n and v[nh][nw] == 2 and (nh, nw) not in sets: # 2가 있으면 그 2도 한 번 해봄
                q.append((nh, nw)) # 더 돌아보고
                sets.add((nh, nw)) # 방문처리
    return False # 주변에 0 없으면 False

n, m = map(int, input().rstrip().split()) # 크기, 가능 갯수
g = [list(map(int, input().rstrip().split())) for _ in range(n)] # 그래프g
vst = [] # 바이러스 시작 지점
for i in range(n):
    for j in range(n):
        if g[i][j] == 2:
            vst.append((i, j))

ans = int(10e9) # 답
for vir in combinations(vst, m): # 조합
    v = [] # 그래프 복사해서 받아 방문처리 할 것
    for i in g:
        v.append(i[:])
    si = set(vir) # 시작점은 bfs에 들어갈 이유 없으나 다른 2는 훑어봐야 하기 때문에 방문처리 따로 관리
    q = deque(vir) # 큐
    fla = True # 갱신 여부 확인
    while q:
        h, w = q.popleft()
        if (h, w) in vst and not (h, w) in si: # 시작점이 아닌 비활성 바이러스 지점이라면
            b = bfs2(h, w) # 2만 bfs하는거 해봐라
            # print(h,w,b)
            if not b: # 참이면 그냥 진행하게 하고, 거짓이면 막힌 것이므로 -1 해주고 다음 반복.
                v[h][w] -= 1 #
                # print(b, h, w, v[h][w])
                continue
        a = v[h][w]+1 # 어찌보면 카운트?
        # if a >= ans: # 시간초가 정답 이상이면 갱신 안할거다.
        #     fla = False
        #     break
        for i in range(4): # 사방탐색
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<n and v[nh][nw] == 0:
                v[nh][nw] = a
                q.append((nh, nw))
            elif 0<=nh<n and 0<=nw<n and v[nh][nw] == 2 and not (nh, nw) in si:
                v[nh][nw] = a
                q.append((nh, nw))
    if fla: # 0이 있으면 갱신 안할거다.
        for i in v:
            if 0 in i:
                fla = False
    if fla: # 그거 아니면 갱신할거임~
        ans = min(ans, max(map(max, *v)))
        # print('======')
        # for i in v:
        #     print(*i)
        # print('======')

if ans != int(10e9): # 갱신이 되었으면 시작값이 2이므로 2 빼서 출력
    print(ans-2)
else: # 끝까지 갱신 안됐다면 0이 무조건 있는 것이므로 -1
    print(-1)
'''


'''
빠른 코드.

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline


index=[[1,0],[-1,0],[0,1],[0,-1]]
now_min=sys.maxsize

def bfs(virus_list,zero_cnt):
    global now_min
    queue=deque()
    visited=[[False for _ in range(n)] for _ in range(n)]
    for v in virus_list:
        vy,vx=v
        queue.append([vy,vx,0])
        visited[vy][vx]=True

    while queue:
        y,x,cnt=queue.popleft()
        if map_data[y][x] == 0:
            zero_cnt -= 1
        if zero_cnt == 0:
            now_min = min(now_min, cnt)
            return
        for indy,indx in index:
            ny=y+indy
            nx=x+indx

        if 0<=nx<n and 0<=ny<n and not visited[ny][nx] and map_data[ny][nx]!=1:
            visited[ny][nx]=True
            queue.append([ny,nx,cnt+1])

                #map_data[ny][nx]=2




n,m=map(int,input().split())
map_data=[list(map(int,input().split())) for _ in range(n)]

zero_cnt=0
possible=[]
for i in range(n):
    for j in range(n):
        if map_data[i][j]==0:
            zero_cnt+=1
        elif map_data[i][j]==2:
            possible.append([i,j])
            #map_data[i][j]=0

comb=combinations(possible,m)

for c in comb:
    bfs(c,zero_cnt)

if now_min==sys.maxsize:
    print(-1)
else:
    print(now_min)
'''