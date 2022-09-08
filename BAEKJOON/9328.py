'''
열쇠

열쇠를 갖고 있고, 일부 열쇠는 빌딩 바닥에 있음. 상하좌우 이동.
훔칠 수 있는 문서의 최대 갯수

입력
테케
h, w 제시. 2이상 100이하
지도
.은 빈 공간 *은 벽 $는 문서 대문자는 문 소문자는 열쇠 스 문자의 대문자인 모든 문을 열 수 있다.
가지고 있는 열쇠가 공백 없이 제시. 없다면 0

출력
훔칠 수 있는 최대 문서
'''
from collections import deque
import sys
input = sys.stdin.readline
# 사방이동
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

for _ in range(int(input())):
    x, y = map(int, input().rstrip().split())
    g = [list(input().rstrip()) for _ in range(x)] # 그래프
    v = [[0]*y for _ in range(x)] # 방문처리
    ans = 0 # 정답
    key = input().rstrip() # 열쇠
    if key == '0': # 0이면 없는거
        key = ''
    else:
        key = key.upper() # 아니면 대문자로
    inn = [] # 들어갈 수 있는 곳
    doors = {} # 문이 있는 곳
    for i in range(x):
        for j in range(y):
            if (i == 0 or i == x-1) or (j == 0 or j == y-1):
                if g[i][j] == '.': # .이면 들어갈 수 있음
                    inn.append((i, j))
                    v[i][j] = 1
                elif g[i][j] == '$': # $도 진입 가능
                    ans += 1
                    v[i][j] = 1
                    inn.append((i, j))
                elif g[i][j] == '*': # *은 진입 불가
                    continue
                elif 97<=ord(g[i][j])<=122: # 소문자 진입 가능
                    v[i][j] = 1
                    key += g[i][j].upper()
                    inn.append((i, j))
                elif 65<=ord(g[i][j])<=90: # 문이라면
                    alp = g[i][j]
                    if alp in key: # 열쇠 갖고 있으면 들어 갈 수 있음
                        v[i][j] = 1
                        inn.append((i, j))
                        continue
                    if doors.get(alp, 0): # 아니면 문 정보에 모아둠
                        doors[alp].append((i, j))
                    else:
                        doors[alp] = [(i, j)]
    q = deque(inn) # 큐
    while q: # bfs
        h, w = q.popleft()
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<x and 0<=nw<y and v[nh][nw] == 0:
                if g[nh][nw] == '.': # .은 감
                    q.append((nh, nw))
                    v[nh][nw] = 1
                elif g[nh][nw] == '$': # $도 감
                    v[nh][nw] = 1
                    q.append((nh, nw))
                    ans += 1
                elif 97<=ord(g[nh][nw])<=122: # 소문자도 감
                    v[nh][nw] = 1
                    key += g[nh][nw].upper()
                    q.append((nh, nw))
                elif 65<=ord(g[nh][nw])<=90: # 대문자는 문 좌표에만 추가할거임.
                    alp = g[nh][nw]
                    if doors.get(alp, 0): # 이미 딕트에 같은 문이 있으면 추가만하고
                        doors[alp].append((nh, nw))
                    else: # 없으면 새로 만들어줌
                        doors[alp] = [(nh, nw)]
        if not q: # 큐가 비어있으면 열쇠가 있는 문 좌표를 딕트로 확인
            for i in key: # 열쇠들 보면서
                if doors.get(i, 0): # 그 열쇠에 맞는 문이 있으면
                    for j in doors[i]: # 따고 큐에 추가
                        q.append((j[0], j[1]))
                        v[j[0]][j[1]] = 1
                    del doors[i] # 그 문 다 땄으니까 지움
    print(ans)



'''
1
3 3
***
Z$*
***
z 
'''







'''
1
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
'''