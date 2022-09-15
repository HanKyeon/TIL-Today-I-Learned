'''
피리 부는 사나이

성우가 피리를 불면 정해놓은 방향대로 이동. UDLR 상하좌우
세이프 존 건설 예정. 최소 세이프 존 갯수

입력
n, m 행렬 1이상 1000이하
지도 제시. 밖으로 안나감

출력
세이프 존의 갯수
'''


import sys
input = sys.stdin.readline

# 방향. g[h][w]를 이용해서 부를 것이다.
di = {'D':(1, 0), 'U':(-1, 0), 'L':(0, -1), 'R':(0, 1)}

def find(h, w): # 조상 찾기
    p = parent[h][w] # 현재 조상
    if (h, w) != p: # 자기 자신을 가르키지 않으면
        parent[h][w] = find(p[0], p[1]) # 찾으러 떠나서 초기화해라
    parent_set.add(parent[h][w]) # 없으면 넣어주고
    return parent[h][w] # 조상 리턴

def union(h1, w1, h2, w2): # 합치기 연산
    a, b = find(h1, w1), find(h2, w2) # a, b는 두 좌표의 조상
    if a == b: # 조상 같으면 끝
        return
    nh1, nw1 = a # 좌
    nh2, nw2 = b # 표
    # 작은쪽에 먹게 할 것
    if nh1 < nh2:
        parent[nh2][nw2] = (nh1, nw1)
        if (nh2, nw2) in parent_set:
            parent_set.remove((nh2, nw2))
    elif nh1 > nh2:
        parent[nh1][nw1] = (nh2, nw2)
        if (nh1, nw1) in parent_set:
            parent_set.remove((nh1, nw1))
    else:
        if nw1 < nw2:
            parent[nh2][nw2] = (nh1, nw1)
            if (nh2, nw2) in parent_set:
                parent_set.remove((nh2, nw2))
        else:
            parent[nh1][nw1] = (nh2, nw2)
            if (nh1, nw1) in parent_set:
                parent_set.remove((nh1, nw1))

def check(h1, w1, h2, w2): # 일단 넣어본 둘이 같은 조상을 가졌다면
    return find(h1, w1) == find(h2, w2)

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
parent = [[(i, j) for j in range(m)] for i in range(n)]
parent_set = set()
for i in range(n):
    for j in range(m):
        dh, dw = di[g[i][j]]
        union(i, j, i+dh, j+dw)
# for i in parent:
#     print(*i)
print(len(parent_set))




# 빠른 코드
import sys
input = sys.stdin.readline

def get_node(x, y):
    return x*M + y

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
    return 

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [input().rstrip() for _ in range(N)]
    parent = [-1 for _ in range (N*M)]
    dir ={'D':(1, 0), 'U':(-1, 0), 'L':(0, -1), 'R':(0, 1)}
    visited = set()
    cnt = 0
    for i in range(N):
        for j in range(M):
            x, y = dir[board[i][j]]
            union(get_node(i, j), get_node(i+x, j+y))
    
    cnt = 0
    for i in range(N*M):
        if parent[i] < 0:
            cnt += 1

    print(cnt)

    for i in parent:
        print(i)
    print(visited)











