'''
격자판의 숫자 이어 붙이기

4*4 격자판. 0~9 숫자 기록.
임의의 위치에서 시작해서 동서남북 네 방향으로 인접한 격자로 총 6회 이동하면서
각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.
이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며
0으로 시작하는 0102001과 같은 수를 만들 수도 있다.
단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.
격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.

입력
테케T
격자 4줄

출력
#테케 서로 다른 7자리 수들의 갯수
'''
from collections import deque

dw = [-1, 1, 0, 0]
dh = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y, g[x][y]))
    while q:
        h, w, s = q.popleft()
        if len(s) == 7:
            sets.add(s)
            continue
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<4 and 0<=nw<4 :
                q.append((nh, nw, s+g[nh][nw]))
    return

def dfs(li, w, h):
    li += (g[w][h])
    if len(li) == 7 and not (li in sets):
        sets.add(li)
        return
    for i in range(4):
        nw, nh = w + dw[i], h + dh[i]
        if 0<=nw<4 and 0<=nh<4 and len(li) <= 6:
            dfs(li,nw,nh)

for testcase in range(1, int(input())+1):
    g = [input().split() for _ in range(4)]
    sets = set()
    for i in range(4):
        for j in range(4):
            # bfs(i, j)
            dfs('', i, j)
    print(f"#{testcase} {len(sets)}")


'''
    for _ in range(6):
        new_nums = [[[] for _ in range(4)] for _ in range(4)]
        for x in range(4):
            for y in range(4):
                tmp = set()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    tx, ty = x + dx, y + dy
                    if tx < 0 or tx == 4 or ty < 0 or ty == 4: continue
                    tmp.update(nums[tx][ty])
                for val in list(tmp):
                    new_nums[x][y].append(val * 10 + arr[x][y])
        nums = new_nums
    tmp = set()
    for x in range(4):
        for y in range(4):
            tmp.update(nums[x][y])
    print('#{} {}'.format(tc, len(tmp)))
'''
'''
from collections import deque

def solution(graph):
    answer = set()
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    for x in range(0, 4):
        for y in range(0, 4):
            start = (x, y, graph[x][y])

            q = deque([start])

            while q:
                cur_x, cur_y, cur_num = q.popleft()

                for i in range(4):
                    nx = cur_x + dx[i]
                    ny = cur_y + dy[i]

                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if len(cur_num) < 6:
                            q.append((nx, ny, cur_num+graph[nx][ny]))
                        else:
                            answer.add(cur_num+graph[nx][ny])
    return len(answer)


for n in range(1, N+1):
    Graph = [list(input().split()) for _ in range(4)]
    print("#%d %d" % (n, solution(Graph)))
'''