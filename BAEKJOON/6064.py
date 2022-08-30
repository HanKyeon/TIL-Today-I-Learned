'''
카잉 달력

첫번째 해를 1:1, 두번째 해 2:2.
x:y 다음 해가 x':y'일 때, x<M이면 x'=x+1이고 그렇지 않으면 x'=1. 같은 방식으로 y<n이면 y'=y+1이고 아니면 y'=1

M:N은 그들 달력의 마지막 해. 세상의 종말이 도래한다는 예언이 전해진다.
예를 들어 M이 10이고 N이 12일 때, 첫째 해는 1:11 11번째는 1:11 3:1은 13번째, 10:12는 마지막 60번째 해이다.
네개의 정수 M N x y 제시 M:N이 마지막해라면, x:y는 몇번째?

입력
테메T
M N X Y 제시. MN은 1이상 4만이하 x는 1이상 M이하 y는 1이상n이하

출력
x:y가 k번째 해일 때 정수 k를 한 줄에 출력. x:y가 유효하지 않다면 -1 출력
'''
for _ in range(int(input())):
    m, n, x, y = map(int, input().split())

    while x <= m*n:
        if (x-y)%n == 0:
            break
        x += m
    if x>m*n:
        print(-1)
    else:
        print(x)




'''
시간초과
    for i in range(1, n*m+1):
        if i % m == x and i % n == y:
            print(i)
            break
    else:
        print(-1)
'''

'''
메모리 초과
    mli = list(range(1, m+1)) * n
    nli = list(range(1, n+1)) * m
    nnl = list(zip(mli, nli))
    if (x,y) in nnl:
        print(nnl.index((x,y)))
    else:
        print(-1)
'''

'''
시간 초과
    a, b, c = 1, 1, 0
    fla = False
    while True:
        print(a, b)
        c+=1
        if a == x and b == y:
            fla = True
            break
        if a == m and b == n:
            break
        if a < m:
            a = a+1
        elif a>= m:
            a = 1
        if b < n:
            b += 1
        elif b >= n:
            b = 1

    if not fla:
        c = -1
    print(c)
'''




















