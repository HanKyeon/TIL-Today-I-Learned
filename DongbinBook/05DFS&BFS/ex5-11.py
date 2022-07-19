'''
n*m 미로. 1,1 시작. 미로 출구는 n, m. 1번에 1번 이동.
괴물이 있으면(벽) 0, 없으면 1. 미로는 반드시 탈출 가능.
이 때, 탈출하기 위해 움직여야 하는 최소 칸의 갯수. 시작 칸 및 마지막 칸 포함.
'''
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n) :
    graph.append(list(map(int, input())))

# 상하좌우 !! 주의점은 x로 묶은 축을 이동하는 dx가 상하이동이다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# bfs 형태로 한다.
def bfs(x, y) :
    # 일단 데크를 하나 추가. 좌표를 계속 큐 자료구조로 받아옴.
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue : 
        x, y = queue.popleft()
        # 현 위치에서 네 방향으로의 위치 확인. 상하좌우 훑으며 좌표를 재봄
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 벗어나면 패스
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            # 벽일 경우 무시
            if graph[nx][ny] == 0 :
                continue
            # next x,y가 길이라면  next x,y는 이전 x,y보다 1 증가시킨다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny)) # 그 후 큐 자료구조에 nx ny를 넣는다.
        # 상하좌우를 확인 한 후 만족하면 append로 넣어주니 다시 popleft로 가까운 노드부터
        # 재귀한다.

        # 가장 오른쪽 아래까지 최소거리 반환. n-1, m-1인 이유는 좌표를 1,1부터 시작시켰기 때문에.
        return graph[n-1][m-1]
# 출발!
print(bfs(0, 0))
