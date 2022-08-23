'''
미로

도착 가능하면 1 아니면 0

입력
테케T
N
지도

출력
#T 1 가능 0 불가능
'''
dh = [1, -1, 0, 0]
dw = [0, 0, 1, -1]

for testcase in range(1, int(input())+1):
    n = int(input())
    g = [list(input()) for _ in range(n)]
    li = []
    for i in range(n):
        for j in range(n):
            if g[i][j] == '2':
                li.append((i, j))
    while li:
        h, w = li.pop(0)
        g[h][w] = '2'
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<n:
                if g[nh][nw] == '0' or g[nh][nw] == '3':
                    li.append((nh,nw))
    ans = 1
    for i in g:
        if '3' in i:
            ans = 0
            break
    print(f"#{testcase} {ans}")








