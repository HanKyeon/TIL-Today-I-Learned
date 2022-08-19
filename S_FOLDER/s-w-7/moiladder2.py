'''
Ladder2

사다리타기 한다. 최단거리로 바닥에 도착하게 되어야 한다.
바닥까지 가장 짧은 이동거리를 갖는 시작점을 반환. 복수개일 경우 가장 큰 좌표.
'''

import sys
sys.stdin = open("input.txt", "r")

# 이동방향. 좌우를 먼저 하여 조건 줄임
dh = [0, 0, 1]
dw = [1, -1, 0]

def dfs(h, w, c, l): # x, y, 숫자, 길이. c를 시작좌표+2로 해서 반환을 c, l로 해서 풀이 가능.
    if h == 99: # 바닥이면 끝
        return l
    g[h][w] = c # 방문처리
    for i in range(3): # 우 좌 하 순으로 확인
        nh, nw = h + dh[i], w + dw[i] # 이동 예정 좌표
        # 좌표 안에 있고, 0 아니고 방문처리 안된 노드들에 한해서 우 좌 하 순으로 확인
        if 0 <= nh < 100 and 0 <= nw < 100 and g[nh][nw] != 0 and g[nh][nw] != c:
            return dfs(nh, nw, c, l+1) # dfs
# 스택으로 하니 메모리 초과 뜬듯?
def 스택(h, w, c, l): # 스택으로 만듬
    li = [(h, w, c, l)] # 리스트에 튜플 추가
    while li: # 빌 때까지
        hh, ww, cc, ll = li.pop() # 추출
        g[hh][ww] = c # 방문처리
        if hh == 99: # 99면 끝
            break
        for i in range(3): # 마찬가지로 우좌하 순서로 순회
            nh, nw = hh + dh[i], ww + dw[i]
            if 0 <= nh < 100 and 0 <= nw < 100 and g[nh][nw] != 0 and g[nh][nw] != cc:
                li.append((nh, nw, c, ll+1))
                break # 추가 했으면 다른 길 추가하지 말고 li.pop하러 떠남
    return ll # l 이 아니라 ll을 반환해줘야함.

for testcase in range(1, 11):
    _ = input() # 의미 없는 입력 받아주기
    g = [list(map(int, input().split())) for _ in range(100)] # 그래프
    sts = [i for i, v in enumerate(g[0]) if v == 1] # 시작 지점
    b = [0] * len(sts) # 시작지점에 따른 길이 저장 할 b
    for i in range(len(sts)): # 그만큼 돌면서 b 채워줘라
        b[i] = 스택(0, sts[i], i+3, 1)
    x = [i for i, v in zip(sts, b) if v == min(b)][-1] # 시작지점 도착지점 zip으로 묶어서 v가 최솟값인 좌표 i의 맨뒤
    print(f"#{testcase} {x}") # 출력


