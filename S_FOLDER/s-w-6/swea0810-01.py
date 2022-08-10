'''
4방향 탐색
'''
def cr(x, y) :
    global n
    c = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n :
            c += abs(g[nx][ny] - g[x][y])
        else : continue
    return c

for testcase in range(1, int(input())+1) :
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    cs = 0
    for i in range(n) :
        for j in range(n) :
            cs += cr(i, j)
    print(f"#{testcase} {cs}")
