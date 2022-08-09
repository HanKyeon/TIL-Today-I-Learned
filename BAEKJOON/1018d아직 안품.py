'''
체스판 다시 칠하기
'''
def chess(x, y) :
    c1, c2 = 0, 0
    l1, l2 = list('WBWBWBWB'), list('BWBWBWBW')
    ch1 = [l1, l2, l1, l2, l1, l2, l1, l2]
    ch2 = [l2, l1, l2, l1, l2, l1, l2, l1]
    
    for i in range(8) :
        for j in range(8) :
            if g[x+i][y+j] != ch1[i][j] :
                c1+=1
            if g[x+i][y+j] != ch2[i][j] :
                c2+=1
    return min(c1, c2)

n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]
mc = n*m
for i in range(n-7) :
    for j in range(m-7) :
        mc = min(mc, chess(i, j))
print(mc)

        


'''
완탐. 어차피 최대가 50 50이니가 걍 for문 돌려도 될듯

W로 시작하는 체스판
B로 시작하는 체스판

WBWBWBWB
BWBWBWBW

ㅁ
'''
