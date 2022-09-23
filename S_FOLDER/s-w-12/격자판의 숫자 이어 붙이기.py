'''
4*4 격자판. 0~9 사이 숫자.
동서남북 네 방향으로 인접한 격자로 여섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 이어 붙이면 7자리수.
이동 할 때 한 번 거쳤던 격자 재방문 가능. 0으로 시작하는 0102001도 가능.
격자판 벗어날 수 없음.
서로 다른 일곱자리 수들의 갯수를 구하시오.

입력
테케T
그래프 제시.

출력
#테케T 7자리 숫자 가능한 갯수
'''
dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def dfs(h, w, val, num):
    if num == 0:
        sets.add(val)
        return
    for i in range(4):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<4 and 0<=nw<4:
            dfs(nh, nw, val + g[nh][nw]*(10**(num-1)), num-1)

for tc in range(1, int(input())+1):
    g = [list(map(int, input().rstrip().split())) for _ in range(4)]
    sets = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, g[i][j]*(10**6), 6)
    print(sets)
    print(f"#{tc} {len(sets)}")


























