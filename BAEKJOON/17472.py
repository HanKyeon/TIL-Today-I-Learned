'''
다리 만들기2

섬나라. 모든 섬을 다리로 연결 할 것.
n*m 2차원 격자.
다리는 바다에만 건설 가능. 다리 길이는 다리가 격자에서 차지하는 칸의 수.
다리 길이는 2 이상, 다리의 방향이 중간에 바뀌면 안된다. 다리 방향은 가로 또는 세로만 가능.

다리가 교차하는 경우가 있다면, 다리의 길이 계산 할 때 각 칸이 각 다리의 길이에 모두 포함되어야 한다.

입력
세로n 가로m 0은 바다 1은 땅

출력
모든 섬을 연결하는 다리 길이 최솟값.
불가능시 -1 출력.
'''
'''
아이디어:

섬마다 bfs를 하며 좌표 리스트(세트)를 만들고 리스트에 담는다. (노드 리스트 형태)
각 섬의 좌표에 대해 1이 없는 쪽으로 1칸씩 직진해서 섬좌표가 있는지 확인. 있다면 길이 반환 후 다른 방향으로. 이 때, 길이가 1 이하라면 담지 않는다. 뚫린 방향에 대해서만 직진하고, 확인하고 직진하고 확인하고 길이를 리턴하고 그 길이를 확인해서 담을지 말지 결정해야 할듯.

이후 dfs 및 백트래킹을 이용해서 다리 길이의 최솟값을 구해주자.
'''
from collections import deque
from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline
'''
상 하 우 좌
'''
dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]
'''
함수 거리구해서담기() 명세

각 섬의 좌표를 훑어서 그 좌표 근처에 0이 있다면 0이 있는 부분으로 쭉 뻗어나간다.
1을 만나면 처음 만난 섬의 번호를 찾아 그 섬까지의 거리에 기록하고, 그 방향 종료한다.
모든 섬의 좌표에 대해 실행하여 모든 섬 간의 거리를 기록한다.

함수 U() D() R() L() : 파라미터로 시작 좌표, 방향, 시작 섬 번호를 받는다.
한방향 쭉 가서 1을 만나면 섬을 찾고 gs[시작섬][도착섬]에 거리를 기록하고, 좌표를 벗어나면 끝내는 함수

함수 본체 :
인덱스로 섬을 훑는다.
섬의 좌표를 훑는다.
섬의 좌표 사방을 확인하여 0인 쪽으로 U() D() R() L()을 시행해주어서 섬 간의 거리 gs를 저장해준다.
'''
def 거리구해서담기(): # 각 섬들의 좌표를 훑으며 주변에 0이 있는 좌표는 쭉쭉 뻗어서 확인하게 만든다.
    global islnum, n, m, g
    def U(h, w, di, idx): # 좌표, 방향, 시작 섬 번호 받아서
        i = 0
        while True:
            i+=1
            nh = h + dh[di]*i # 위쪽으로만 쭉 진행해서
            if nh<0 or nh>=n: # 벗어나면 끝
                return
            if g[nh][w] == 1: # 1 만나면
                for j in range(islnum): # 그 좌표 있는 섬 번호 찾아서
                    if (nh, w) in islands[j]:
                        if i >= 3 and idx != j: # 길이가 2 이상이어야 기록함
                            gs[idx][j] = min(gs[idx][j], i-1) # 간선 길이 그래프에 넣고 끝
                        return
    def D(h, w, di, idx): # 아랫방향으로 동일하게 시행
        i = 0
        while True:
            i+=1
            nh = h + dh[di]*i
            if nh<0 or nh>=n:
                return
            if g[nh][w] == 1:
                for j in range(islnum):
                    if (nh, w) in islands[j]:
                        if i >= 3 and idx != j:
                            # print(f"{idx}번째 섬에서 {j}번째 섬 거리 {i-1}")
                            gs[idx][j] = min(gs[idx][j], i-1)
                            # gs[j][idx] = min(gs[j][idx], i-1)
                        return
    def R(h, w, di, idx): # 우측 방향으로 동일하게 시행
        i = 0
        while True:
            i+=1
            nw = w + dw[di]*i
            if nw<0 or nw>=m:
                return
            if g[h][nw] == 1:
                for j in range(islnum):
                    if (h, nw) in islands[j]:
                        if i >= 3 and idx != j:
                            gs[idx][j] = min(gs[idx][j], i-1)
                        return
    def L(h, w, di, idx): # 왼쪽 방향으로 동일하게 시행
        i = 0
        while True:
            i+=1
            nw = w + dw[di]*i
            if nw<0 or nw>=m:
                return
            if g[h][nw] == 1:
                for j in range(islnum):
                    if (h, nw) in islands[j]:
                        if i >= 3 and idx != j:
                            gs[idx][j] = min(gs[idx][j], i-1)
                        return

    for i in range(islnum): # 번호로 섬을 훑는데
        for j in islands[i]: # 섬좌표들을 훑을거다.
            for l in range(4): # 각 좌표에서 사방을 확인해서
                nh, nw = j[0] + dh[l], j[1] + dw[l]
                if 0<=nh<n and 0<=nw<m and g[nh][nw] == 0: # 범위 내이고 0이 있다면
                    if l == 0: # 위쪽이면 위쪽 실행
                        # print(j[0], j[1], "U 실행", f"{i}번째 섬")
                        U(j[0], j[1], l, i)
                    elif l == 1: # 아래쪽이면 아래쪽 실행
                        # print(j[0], j[1], "d 실행", f"{i}번째 섬")
                        D(j[0], j[1], l, i)
                    elif l == 2: # 우측이면 우측
                        # print(j[0], j[1], "r 실행", f"{i}번째 섬")
                        R(j[0], j[1], l, i)
                    elif l == 3: # 좌측이면 좌측 실행
                        # print(j[0], j[1], "L 실행", f"{i}번째 섬")
                        L(j[0], j[1], l, i)
'''

# 함수 최솟값찾기() 명세

# DFS와 백트래킹을 하면 최소 거리가 나올 것이라 생각하고 만들었으나, 실효성은 없었음.

def 최솟값찾기(idx, num):
    global ans
    print(idx, num)
    if num >=ans:
        return
    if sum(vi) == islnum:
        ans = min(num, ans)
        return
    for i in range(islnum):
        if gs[idx][i] != int(10e9) and vi[i] == 0:
            vi[i] = 1
            최솟값찾기(i, num+gs[idx][i])
            vi[i] = 0
'''
n, m = map(int, input().split()) # 세로n 가로m
g = [list(map(int, input().rstrip().split())) for _ in range(n)] # 지도
v = [] # 방문처리용 복사한 g
for i in g:
    v.append(i[:])
islands = [] # 섬의 좌표들
for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and v[i][j] == 1: # 그래프 순회하면서 방문 안된 것들 bfs 실행하여 섬좌표를 islands에 담음.
            q = deque([(i, j)])
            jwapyo = set([(i, j)])
            v[i][j] = 0
            while q:
                h, w = q.popleft()
                for k in range(4):
                    nh, nw = h + dh[k], w + dw[k]
                    if 0<=nh<n and 0<=nw<m and g[nh][nw] == 1 and v[nh][nw] == 1:
                        v[nh][nw] = 0
                        q.append((nh, nw))
                        jwapyo.add((nh, nw))
            islands.append(jwapyo)
# for i in islands:
#     print(i)
islnum = len(islands) # 섬 갯수
gs = [[int(10e9) for _ in range(islnum)] for _ in range(islnum)] # 간선 정보들. 섬간의 거리 최솟값을 담을 것이기 때문에 빼줌.
거리구해서담기()
# for i in gs:
#     print(*i)

# 거리 짧은 순으로 힙에 담아줄 것
heap = []
for i in range(islnum):
    for j in range(islnum):
        if gs[i][j] != int(10e9):
            heappush(heap, (gs[i][j], i, j))

vi = [0]*islnum
b = []
ans = 0
cc = 0
while heap: # 전부 돌 것임.
    cl, sta, end = heappop(heap)
    # print(cl, sta, end, "거, 시, 도")
    if not b:
        b.append([[cl], sta, end])
        # print(f"{sta}랑 {end} 초기")
    elif b:
        fla = False
        for i in b: # 두개 다 있으면 ㅌㅌ
            if sta in i and end in i:
                fla = True
                break
            elif sta in i and not end in i: # 하나 있으면 추가
                i[0].append(cl)
                i.append(end)
                fla = True
                # print(f"{i}에 {sta}랑 {end} 연결")
                break
            elif not sta in i and end in i: # 하나 있으면 추가
                i[0].append(cl)
                i.append(sta)
                fla = True
                # print(f"{i}에 {sta}랑 {end} 연결")
                break
        if not fla: # 두개 다 없으면 새로 추가
            b.append([[cl], sta, end])
    if len(b)>1: # 두개 이상 있으면 교점 있나 확인하고, 있으면 합쳐줌
        for i in range(1, len(b)):
            li = b[i][0]
            nls = b[i][1:]
            b0 = b[0][0]
            b0s = b[0][1:]
            # print(b0, li, b0s, nls, "이게 4개")
            if len(set(nls) & set(b0s)) == 1:
                uni = list(set(nls) | set(b0s))
                b0 += li
                # print(uni, b0)
                b[0] = [b0]+uni

if b and len(b[0]) == islnum+1:
    print(sum(b[0][0]))
else:
    print(-1)

'''
if sta in b and end in b:
        continue
    if not b:
        b.add(sta)
        b.add(end)
        cc += cl
    elif b:
        if not sta in b and end in b:
            b.add(sta)
        if not end in b and sta in b:
            b.add(end)
        cc += cl
    if len(b[0]) == islnum:
        ans = cc

if not ans:
    ans = -1
if len(islands) == 1:
    ans = 0
print(ans)
'''
'''
ans = int(10e9)
for i in range(islnum):
    vi = [0] * islnum
    vi[i] = 1
    최솟값찾기(i, 0)
    vi[i] = 0

if ans == int(10e9):
    ans = -1
print(ans)

'''
'''
섬 좌표 : islands
방문 여부 vi
즉 섬의 번호는 0 ~ islnum-1 까지
섬 거리 좌표 : gs
최단거리. bfs.
'''




'''
4 8
0 0 0 0 0 0 1 1
1 0 0 1 1 0 1 1
1 1 1 1 0 0 0 0
1 1 0 0 0 1 1 0
5

10 6
0 0 0 1 0 0
0 0 0 1 0 0
0 1 0 0 0 1
0 0 0 0 0 0
1 1 0 1 1 0
1 0 0 0 1 0
1 1 0 0 1 0
0 0 0 0 1 1
0 0 0 0 0 0
0 1 0 0 0 0

13
'''
'''
10 10
0 0 0 1 1 0 0 0 0 0
0 0 0 1 0 0 0 0 0 1
0 0 0 1 1 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0
1 0 0 1 0 0 0 0 0 1
0 0 0 1 1 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1
0 0 1 1 1 1 0 0 1 1
'''









