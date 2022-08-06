'''
lader2

'''
# 그래프, y, x, 다른 값으로 해서 그래프 하나로 다중방문 가능하게 idx 추가.
def dfs(g, y, x, idx, c) :
    # 종료 조건. 이번에는 x, c 반환
    if y == 0 :
        return (c, x)
    # 반환해야 하므로 return을 dfs로 줌
    if 0 <= x < 99 and g[y][x+1] != 0 and g[y][x+1] != idx :
        c += 1
        g[y][x+1] = idx
        return(dfs(g, y, x+1, idx, c))
    elif 0 < x <= 99 and g[y][x-1] != 0 and g[y][x-1] != idx :
        c += 1
        g[y][x-1] = idx
        return(dfs(g, y, x-1, idx, c))
    # 불가능하면 위로 이동
    elif g[y-1][x] != 0 :
        c += 1
        g[y-1][x] = idx
        return(dfs(g, y-1, x, idx, c))


for t in range(1, 11) :
    # 입력. t는 반복 시작하면서 입력 받는 값
    ssss = int(input())
    g = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    xs = [i for i, v in enumerate(g[99]) if v == 1]
    cx = []
    
    for idx, x in enumerate(xs) :
        g[y][x] = idx+2 # dfs를 실행하기 전에 자기 위치를 방문처리 해줘야함....
        cx.append(dfs(g, y, x, idx+2, 0))
    # cx를 x[0]는 그대로, x[1]은 음수로해서 역정렬
    cx.sort(key=lambda x:(x[0], -x[1]))
    # 제일 작고 x가 가장 큰 값 반환
    print(f"#{t} {cx[0][1]}")
