'''
ladder1

사다리가 100개인데 인덱스 0을 추가 안하고 바로 받으므로
99, 99에서 dfs처럼 위로 직진하며 좌우 이동 가능하면 좌우이동하게.

주의점은 보통 n,m이라 할 때 y축 이동 n, x축이동 m 각각 담당하는데
이건 수학문제처럼 x이동 x축 y이동 y축 그대로다. 근데 사실 상관 없어보이네 역으로 갈거니까
목표 = dt[99].index(2) 해서 인덱스 찾고
99, 목표에서 이동하면서 가자고~ 3방향만 신경쓰면 된다. 위로, 좌우로.
기본적으로 위로 이동하는데 좌우에 1이면 이동하며 2로 처리

입력 : 테이블

출력 : #테스트케이스 x좌표(인덱스+1)
'''
def dfs(g, y, x) :
    # 종료 조건
    if 2 in g[0] :
        return
    # 좌우 이동 가능하면 방문처리 후 좌우 dfs 실행
    if 0 <= x < 99 and g[y][x+1] == 1 :
        g[y][x+1] = 2
        dfs(g, y, x+1)
    elif 0 < x <= 99 and g[y][x-1] == 1 :
        g[y][x-1] = 2
        dfs(g, y, x-1)
    # 불가능하면 위로 이동
    elif g[y-1][x] == 1 :
        g[y-1][x] = 2
        dfs(g, y-1, x)

for t in range(1, 11) :
    # 입력. t는 반복 시작하면서 입력 받는 값
    ssss = int(input())
    g = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    x = g[y].index(2)
    dfs(g, y, x)
    print(f"#{t} {g[0].index(2)}")





