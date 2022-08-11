'''
색칠하기

입력
테케 1이상 50이하
박스 갯수
x1 y1 x2 y2 색깔 1빨강 2파랑

'''
def fi3(li) :
    c = 0
    for i in li :
        if i == 3 :
            c+=1
    return c

for testcase in range(1, int(input())+1) :
    n = int(input())
    bs = [list(map(int, input().split())) for _ in range(n)]
    g = [[0]*11 for _ in range(11)]
    
    red, blue = [bx for bx in bs if bx[4] == 1], [bx for bx in bs if bx[4] == 2]
    print(red, blue)
    for bd in bs :
        for i in range(bd[1], bd[3]+1):
            for j in range(bd[0], bd[2]+1) :
                g[i][j] += bd[4]
    c = 0
    for bx in g :
        c += fi3(bx)
    print(f"#{testcase} {c}")