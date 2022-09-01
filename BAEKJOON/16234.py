'''
인구 이동

n*n 땅. 칸마다 나라 존재. r행c열 나라엔 a[r][c]명 살고 있음. 국경 존재.
인구이동은 하루동안 아래처럼 진행. 더 이상 인구 이동이 없을 때까지 지속.

1. 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
2. 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
3. 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
4. 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
5. 연합을 해체하고, 모든 국경선을 닫는다.

인구 이동이 몇일동안 지속되는지?

입력
N L R 제시. 1이상50이하 N 1이상 100이하 L R R이 L보다 큼
N개 줄에 각 나라의 인구수. 각 값은 0이상 100이하
인구 이동이 바랫ㅇ하는 일수가 2000이하인 입력만 제시됨.

출력
인구 이동이 며칠 동안 발생하는지?
'''

'''
set에 좌표를 저장하면서 인구수 값의 합을 저장한다. 방문처리.
set를 pop하며 그래프 갱신.
방문처리 안 된 지점 bfs.
v가 모두 차면 v 초기화, 추가 bfs, 일수 증가.
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]

def bfs(h, w):
    global fla, n, l, r # 차이가 l명 이상 r명 이하
    v[h][w] = 1
    q, sets = deque(), set() # 큐, 갱신해줄 좌표 담을 set
    q.append((h, w))
    sets.add((h, w))
    cz = 0 # 각 나라의 합들
    while q: # 평범한 bfs
        h, w = q.popleft()
        cz += g[h][w]
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<n and v[nh][nw] == 0 and l<=abs(g[h][w]-g[nh][nw])<=r:
                v[nh][nw] = 1
                q.append((nh, nw))
                sets.add((nh, nw))
    ret = len(sets) # 리턴값
    val = cz // len(sets) # 갱신해줄 값
    while sets: # 갱신
        a,b = sets.pop()
        g[a][b] = val
    return ret

n, l, r = map(int, input().split()) # 입력
g = [list(map(int, input().rstrip().split())) for _ in range(n)] # 그래프

fla = True # 변화가 없는지 확인해주는 값
ans = -1 # 확인 작업 상 한 번 더 실행하게 되서 -1로 시작
while fla: # 변화가 있다면 반복
    ans += 1
    v = [[0]*n for _ in range(n)] # 방문
    li = [] # 변화 여부 확인 근거
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                li.append(bfs(i, j))
    if len(li) == n**2: # 모든 칸에 방문처리를 1번 씩 헀다면
        fla = False # 변화가 없는 것이다.
print(ans)



'''
# 빠르다!

# 인구 이동
# 백준 16234
# https://www.acmicpc.net/problem/16234
# 14:25 - 
# avg 대입과정 최적화
# 찾는 범위를 벽돌쌓듯 진행
# 이전에 avg를 구한범위 근처만 조사할수있도록 변경

from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
check = [[0]*N for _ in range(N)]
flag = False

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, check, pos_tmp):
    global flag
    q = deque()
    q.append((x, y))
    
    cal_list = [(x, y)]
    sum = graph[x][y]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if check[nx][ny]:
                continue
            if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                q.append((nx, ny))
                cal_list.append((nx, ny))
                sum += graph[nx][ny]
                check[nx][ny] = 1
    
    if len(cal_list) > 1:
        flag = True
        avg = sum // len(cal_list)
        for x, y in cal_list:
            graph[x][y] = avg
            pos_tmp.append((x, y))

def solution():
    day = 0
    global flag

    pos = [(x, y) for x in range(N) for y in range(x%2, N, 2)]
    while True:
        flag = False
        pos_tmp = list()
        check = [[0]*N for _ in range(N)]

        for x, y in pos:
            if not check[x][y]:
                check[x][y] = 1
                bfs(x, y, check, pos_tmp)
        if not flag:
            return day

        day += 1
        pos = pos_tmp
        
                    
if __name__ == "__main__":
    print(solution())
'''








