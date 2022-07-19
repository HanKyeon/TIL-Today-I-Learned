'''
n*m 미로. 1,1 시작. 미로 출구는 n, m. 1번에 1번 이동.
괴물이 있으면 0, 없으면 1. 미로는 반드시 탈출 가능.
이 때, 탈출하기 위해 움직여야 하는 최소 칸의 갯수. 시작 칸 및 마지막 칸 포함.
'''
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n) :
    graph.append(list(map(int, input())))

#상하좌우 !! 주의점은 x로 묶은 축을 이동하는 dx가 상하이동이다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    
    queue = deque()
    queue.append((x, y))

    while queue : 
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue

            if graph[nx][ny] == 0 :
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

        return graph[n-1][m-1]

print(bfs(0, 0))
