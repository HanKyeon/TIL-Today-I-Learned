'''
행렬 찾기

n*n 창고에 네모로 저장.
네모를 찾아 네모의 정보 출력

입력
테케 갯수
100이하의 n
n*n 행렬 정보 숫자로 제시
행렬의 길이가 곂치지 않음.

행렬의 크기를 찾아내고 해당 범위를 전부 0으로 처리

출력
#1 #2 #3 + 행렬 갯수
행렬곱이 작은 순서로, 세로가 긴 것 부터 제시.
'''
# 행렬찾기 함수
def findgraph(h, w) :
    # 가로길이
    def cw(wx) :
        c = 0
        while wx + c < n and g[h][wx + c] != 0 :
            c += 1
        return c
    # 세로길이
    def ch(wh) :
        c = 0
        while wh + c < n and g[wh + c][w] != 0 :
            c += 1
        return c
    # 방문처리
    hl = ch(h)
    wl = cw(w)
    for i in range(h, h + hl) :
        for j in range(w, w + wl) :
            g[i][j] = 0
    # 넓기 및 행렬 길이 반환
    return (hl * wl, hl, wl)

# 그냥 t !!!!!! 그냥 t !!!!!!!!!! 그냥 t !!!!!!!!
for t in range(1, int(input())+1) :
    # 입력
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    data = []
    # 실행
    for y in range(n) :
        for x in range(n) :
            if g[y][x] != 0 :
                data.append(findgraph(y, x))
    # 출력
    data.sort()
    print(f"#{t} {len(data)}", end=' ')
    for i in range(len(data)) :
        print(f"{data[i][1]} {data[i][2]}", end=' ')
    print()

    




