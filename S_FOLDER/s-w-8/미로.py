'''
마지막 줄 2에서 출발해 0인 통로를 따라 3에 도착 할 수 있는지 확인

테케T
N 제시
N N 미로 제시

#테케 도착가능1 불가0
'''

from collections import deque
# 사방이동
dw = [1, -1, 0, 0]
dh = [0, 0, 1, -1]

for testcase in range(1, int(input())+1):
    # 입력
    n = int(input())
    g, v = [input() for _ in range(n)], [[0]*n for _ in range(n)] # 그래프, 방문처리
    sta = None # 시작 지점
    for i in range(n):
        for j in range(n):
            if g[i][j] == '2':
                sta = (i,j) # 시작 지점 저장
                v[i][j] = 1 # 초기 위치 방문처리
        if sta: break
    # BFS
    q = deque()
    q.append(sta)
    ans = 0
    while q:
        h, w = q.popleft()
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<n and g[nh][nw] == '3': # 범위내이고 3 찾았으면
                ans = 1 # 답 있다 하고
                break # 반복문 끝
            elif 0<=nh<n and 0<=nw<n and v[nh][nw] == 0 and g[nh][nw] == '0':
                v[nh][nw] = 1 # 방문처리하고
                q.append((nh, nw)) # 큐에 삽입
        if ans == 1: # 정답 있으면
            break # 그만
    # 출력
    print(f"#{testcase} {ans}")