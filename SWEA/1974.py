'''
스도쿠 검증

정답1 오답0

입력
테케 갯수
9*9 퍼즐 제시

출력
#1 정답여부
#2 정답여부
'''
# 스도쿠 검증
def sudoku(g) :
    # 작은 네모 검증
    def mininemo(x,y) :
        nemo33 = []
        for i in range(x, x+3) :
            for j in range(y, y+3) :
                nemo33.append(g[i][j])
        if len(set(nemo33)) != 9 :
            return 0
        return 1
    # g(xy)의 반대인 s(yx)
    s = [[0] * 9 for _ in range(9)]
    for i in range(9) :
        for j in range(9) :
            s[i][j] = g[j][i]
    sta = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    # 가로 세로 검증
    for x in range(9) :
        if len(set(g[x])) != 9 :
            return 0
        if len(set(s[x])) != 9 :
            return 0
    # 미니네모 검증
    for f in sta :
        if not mininemo(f[0], f[1]) :
            return 0
    return 1


# testcase!!!!!!
for testcase in range(1, int(input())+1) :
    #입력
    g = [list(map(int, input().split())) for _ in range(9)]
    #출력
    print(f"#{testcase}", end=' ')
    print(sudoku(g))




