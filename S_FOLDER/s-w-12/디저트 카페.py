'''
디저트 카페

디저트 카페 갈것. n*n에 모여있음.
내부 숫자는 디저트 종류
대각이동 가능한 길 존재.
대각선 모양, 사각형을 그리며 출발한 카페로 돌아와야 한다. 같은 디저트 팔고 있는 카페는 가지 못한다.
하나만 먹지 못한다.
되돌아 가는 것 안된다.
디저트 많이 먹을거다.
입력으로 주어졌을 때, 대각선으로 움직이고, 서로 다른 디저트를 먹으면서 돌아오는 경우 가장 많이 먹을 수 있는 디저트 수는? 디저트 못먹으면 -1 출력

입력
테케T
길이n
그래프

출력
테케t
#t 답. 못먹으면 -1
'''
dh = [1, 1, -1, -1]
dw = [1, -1, -1, 1]

def dfs(h, w, di, tg):
    global ans, n
    # print(sets)
    for i in range(2):
        nh, nw = h+dh[(di+i)%4], w+dw[(di+i)%4]
        # print(nh, nw, (di+i)%4, tg)
        if (nh, nw, (di+i)%4) == tg:
            # print(sets, '갱신')
            ans = max(ans, len(sets))
            continue
        if 0<=nh<n and 0<=nw<n and g[nh][nw] not in sets:
            sets.add(g[nh][nw])
            dfs(nh, nw, (di+i)%4, tg)
            sets.remove(g[nh][nw])


for tc in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    sets = set()
    ans = -1
    for i in range(n):
        for j in range(i, n):
            if not i and not j: continue
            if i==n-1 and j==n-1: continue
            sets.add(g[i][j])
            dfs(i, j, 0, (i, j, 3))
            sets.remove(g[i][j])
    print(f"#{tc} {ans}")




'''
1
4
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
'''
















