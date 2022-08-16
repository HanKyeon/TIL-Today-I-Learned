'''
정사각형 방

N^2개의 방이 N*N 형태로 늘어서 있다.
위에서 i번째 줄 j번째 방에는 1이상 N^2이하의 수aij가 적혀 있으며 방마다 다르다.
방에서 상하좌우 이동 가능.
but, 이동하려는 방의 숫자가 현재 방보다 1 커야 이동 가능하다.
어떤 수가 적힌 방에서 있어야 가장 많은 갯수의 방을 이동 할 수 있는지?

입력
첫째줄에 T
정수 N 1이상 1000이하
i, j에 숫자가 뭐 들었는지 알려줌 2차원 배열로

출력
#테스트케이스 end=' '
시작방번호 end=' '
최대 이동 가능한 방 갯수
'''
import sys
sys.stdin = open("input.txt", "r")

# 이동
dh = [1, -1, 0, 0]
dw = [0, 0, 1, -1]
# bfs
def bfs(h, w, c): # 세로 가로 카운트
    global n
    li = [(h,w,c)] # li에 초기값 넣기
    maxc = 0 # 최대 c 값 기록용
    while li: # li가 빌 때까지
        nh, nw, nc = li.pop(0) # 덱 사용 대신 0번 인덱스를 빼는 pop(0) 사용
        if nc > maxc: # 카운트가 maxc보다 크면 maxc에 기록
            maxc = nc
        for i in range(4): # 4방향 해볼거다
            rnh, rnw = nh+dh[i], nw+dw[i] # 갈 좌표
            if 0 <= rnh < n and 0 <= rnw < n and g[rnh][rnw] == g[nh][nw]+1: # 가 범위 내이고 이전 값보다 1 크다면
                li.append((rnh, rnw, nc+1)) # 리스트에 튜플 형태로 (h, w, c) 형태로 넣어준다. nc+1로 해줘서 카운트를 늘려준다.
                # 이 때 리스트에 새로 추가되므로 while문이 돌아간다.
    return (g[h][w], maxc) # g[h][w]에서 시작 할 때 maxc가 몇인지 반환

for testcase in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    ma = (0, 0) # 값 기록용
    for i in range(n):
        for j in range(n): # 모든 i, j에 대해 bfs 실행
            nma = bfs(i, j, 1) # i, j를 시작점1로 삼아서 bfs 했을 때 (g[i][j], 최대방)을 받는 변수
            if ma[1] < nma[1]: # 최댓값이 더 크면
                ma = nma # 갱신
            elif ma[1] == nma[1]: # 최댓값이 같으면
                if ma[0] > nma[0]: # 시작값이 작은놈으로
                    ma = nma # 바꿔줌
    print(f"#{testcase} {ma[0]} {ma[1]}") # 출력



