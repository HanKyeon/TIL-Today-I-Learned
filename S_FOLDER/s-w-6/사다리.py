# 위로 이동 없음
dh = [0, 0, 1]
dw = [-1, 1, 0]

def lad(g, h, w, c) :
    lg = 100 # lg는 len(g)
    if h == 99 and g[h][w] == 2 :
        return True
    elif h == 99 :
        return False
    g[h][w] = c
    for i in range(3) :
        nh, nw = h + dh[i], w + dw[i]
        if 0 <= nw < lg and 0 <= nh < lg and g[nh][nw] != 0 and g[nh][nw] != c :
            return lad(g, nh, nw, c)

for testcase in range(1, 11) :
    _ = input()
    g = [list(map(int, input().split())) for _ in range(100)]
    sta = [i for i, v in enumerate(g[0]) if v == 1]

    for st in sta :
        s = lad(g, 0, st, st + 3)
        if s :
            print(f"#{testcase} {st}")
            break



