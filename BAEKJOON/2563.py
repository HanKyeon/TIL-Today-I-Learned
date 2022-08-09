'''
색종이

가로세로 100인 

입력
가로 세로 100 정사각형 도화지
10 * 10 검은 색종이를 여러장 붙일 것이다.
두개의 자연수로 주어짐.
1은 왼쪽 변 사이의 거리, 2는 아래쪽 변과 도화지 사이의 거리
즉, 좌하단 좌표 제공. 
색종이가 도화지 밖으로 나가는 경우는 없음.

출력
색종이가 붙은 검은 영역의 넓이 출력.
'''

'''
from collections import deque
# bfs 방식
def blackbox(xy) :
    q = deque()
    q.append([xy[0], xy[1]])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q :
        edge = q.popleft()
        x, y = edge
        g[x][y] = 1
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if xy[0] <= nx < xy[0] + 10 and xy[1] <= ny < xy[1] + 10 and g[nx][ny] != 1 :
                q.append(([nx, ny]))
'''
# bfs 그딴거 없이 그냥 칠하기
def blackbox2(xy) :
    for x in range(10) :
        for y in range(10) :
            if g[xy[0] + x][xy[1] + y] == 1 :
                continue
            g[xy[0] + x][xy[1] + y] = 1
# 입력
n = int(input())
pl = [list(map(int, input().split())) for _ in range(n)]
g = [[0]*100 for _ in range(100)]
# 실행
for j in pl :
    blackbox2(j)
hap = 0
for k in range(100) :
    hap += sum(g[k])
# 출력
print(hap)


