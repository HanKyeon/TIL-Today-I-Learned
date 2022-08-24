'''
색종이 만들기

입력
전체 종이의 한 변N. 2 4 8 16 32 64 128 중 하나.
그래프 제시.

출력
하얀색 색종이의 갯수 0
파란색 색종이의 갯수 1
'''
def wb(h1, w1, h2, w2):
    if h2-h1 <= 1 or w2-w1 <= 1:
        whbl[g[h1][w1]] += 1
        return
    s = 0
    for i in range(h1, h2):
        for j in range(w1, w2):
            s += g[i][j]
            if s and g[i][j] == 0:
                break
        if s and g[i][j] == 0:
            break
    sb = (h2-h1) * (w2-w1)
    midh, midw = (h2+h1)//2, (w2+w1)//2
    if s == 0:
        whbl[0] += 1
        return
    elif s == sb:
        whbl[1] += 1
        return
    return wb(h1, w1, midh, midw), wb(midh, w1, h2, midw), wb(h1, midw, midh, w2), wb(midh, midw, h2, w2)

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
whbl = [0, 0]
wb(0, 0, n, n)
print(whbl[0])
print(whbl[1])



'''
s = 0
    for i in range(h1, h2):
        for j in range(w1, w2):
            s += g[i][j]
            if s and g[i][j] == 0:
                break
        if s and g[i][j] == 0:
            break
'''