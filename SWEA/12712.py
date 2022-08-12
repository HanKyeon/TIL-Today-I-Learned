'''
파리 퇴치 3

N은 5 이상 15이하
M은 2이상 N이하
파리갯수 30이하
'''
def cro(x, y) :
    global n
    global m
    s1, s2 = g[x][y], g[x][y]
    for i in range(1, m+1):
        s1 += g[x+i][y] + g[x-i][y] + g[x][y-i] + g[x][y+i]
        s2 += g[x+i][y+i] + g[x-i][y-i] + g[x+i][y-i] + g[x-i][y+i]

        # else : # 0 <= x < m and 0 <= y < m
        #     if x-i < 0 and y-i < 0 : # 좌상
        #         s1 += g[x + i][y] + g[x][y + i]
        #         s2 += g[x + i][y + i]
        #     elif x + i >= n - m and y-i < 0 : # 좌하
        #         s1 += g[x - i][y] + g[x][y + i]
        #         s2 += g[x - i][y + i]
        #     elif x-i < 0 and y+i >= n-m : # 우상
        #         s1 += g[x + i][y] + g[x][y - i]
        #         s2 += g[x + i][y - i]
        #     elif x + i >= n-m and y + i >= n-m : # 우하
        #         s1 += g[x - i][y] + g[x][y - i]
        #         s2 += g[x - i][y - i]
        #
        #     elif x - i < 0: # 상
        #         s1 += g[x + i][y] + g[x][y - i] + g[x][y + i]
        #         s2 += g[x + i][y + i] + g[x + i][y - i]
        #     elif y - i < 0 : # 좌
        #         s1 += g[x + i][y] + g[x - i][y] + g[x][y + i]
        #         s2 += g[x + i][y + i] + g[x - i][y + i]
        #     elif x + i >= n-m :
        #         s1 += g[x - i][y] + g[x][y - i] + g[x][y + i]
        #         s2 += g[x - i][y - i] + g[x - i][y + i]
        #     elif y + i >= n-m :
        #         s1 += g[x + i][y] + g[x - i][y] + g[x][y - i]
        #         s2 += g[x - i][y - i] + g[x + i][y - i]
    return max(s1, s2)


for testcase in range(1, int(input())+1) :
    n, m = map(int, input().split())
    m = m-1
    ud = [[0]*(n+2*m)]
    g = [[0]*m + list(map(int, input().split())) + [0]*m for _ in range(n)]
    g = ud * m + g + ud * m
    d = []
    for a in range(m, n+m):
        for b in range(m, n+m):
            d += [cro(a, b)]
    print(f"#{testcase} {max(d)}")


