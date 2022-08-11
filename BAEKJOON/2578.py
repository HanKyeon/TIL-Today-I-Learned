'''
빙고

25칸 빙고. 1부터 25 자연수
진행에 따라 빙고.
가로/세로/대각이 모두 지워지면 빙고
철수 판떼기 기준 몇번만에 빙고 나옴?

입력
철수 판떼기 선입력 25개
사회자 번호 후입력 25개

출력
사회자의 몇번째 번호에 철수가 빙고 뜨는지?
'''
def bingo(num) :
    global c
    c+=1
    d = 0
    for i in range(5) :
        for j in range(5) :
            if g[i][j] == num :
                g[i][j] = 0
    s = list(map(list, zip(*g)))
    cro = [0, 0]
    for i in range(5) :
        if sum(g[i]) == 0 :
            d += 1
        if sum(s[i]) == 0 :
            d += 1
        cro[0] += g[i][i]
        cro[1] += g[i][4-i]

    d += cro.count(0)
    if d >= 3 :
        return c
    return False


g = [list(map(int, input().split())) for _ in range(5)]
nc = []
for _ in range(5) :
    nc += list(map(int, input().split()))
c = 0
for n in nc :
    a = bingo(n)
    if a :
        print(a)
        break


