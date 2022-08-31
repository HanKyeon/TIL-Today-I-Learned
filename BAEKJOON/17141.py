'''
연구소2

바이러스 유출 할 것.
특정 위치에 바이러스 M개를 놓을 것이다.
연구소의 상태가 주어졌을 때 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간.

입력
연구소의 크기 5이상 50이하 n, 바이러스 갯수 m 1이상 10이하
연구소 상태 제시. 0은 빈 칸, 1은 벽, 2는 바이러스 가능 칸. 2의 갯수는 m이상 10이하 자연수

출력
연구소 감염시키는 최소 시간. 어떻게 놓아도 바이러스를 퍼뜨릴 수 없는 경우 -1 출력
'''

from collections import deque
from itertools import combinations


n, m = map(int, input().rstrip().split()) # 크기, 바이러스 갯수
g = [list(map(int, input().rstrip().split())) for _ in range(n)] # 그래프
vsp = [] # 바이러스 가능 스팟
for i in range(n):
    for j in range(n):
        if g[i][j] == 2:
            vsp.append((i, j))
# 사방이동
dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]
ans = int(10e9)
for i in combinations(vsp, m): # 바이러스 시작점 조합
    si = set(i) # 바이러스를 둔 좌표모음
    q = deque(i)
    v = []
    for ng in g: # 그래프 복사
        v.append(ng[:])
    fla = True # 값 갱신 여부 확인
    while q:
        h, w = q.popleft()
        if not fla: # 끝까지 안해서 거짓 떴으면 돔황챠
            break
        for k in range(4):
            nh, nw = h+dh[k], w+dw[k]
            # 범위 내인데 방문 안했거나 2인데 바이러스를 둔 곳이 아니라면
            if 0<=nh<n and 0<=nw<n and (v[nh][nw] == 0 or (v[nh][nw] == 2 and not (nh, nw) in si)):
                a = v[h][w]+1
                v[nh][nw] = a
                if a >= ans: # 중간에 저장된 ans보다 값이 커지면 == 시간이 길어지면
                    fla = False # 저장 안할거임
                    break
                q.append((nh, nw))
    if fla: # 0있으면 갱신 안함
        for j in v:
            if 0 in j:
                fla = False
                break
    if fla: # 험난한 길 뚫고 참이면 갱신
        ans = min(ans, (max(map(max, *v))))
if ans == int(10e9): # 안바꼈으면
    ans = -1 # -1
    print(ans)
else:
    print(ans-2) # 2에서 카운트 시작했으므로 뺌
'''
7 3
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2

7 4
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2

5 4
'''