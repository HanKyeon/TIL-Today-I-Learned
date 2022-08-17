'''
별 찍기 - 10

재귀적인 패턴으로 별을 찍어보자.
N이 3의 거듭제곱이라고 할 때, 크기 N의 패턴은 N*N 정사각형이고
가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
n이 3보다 클 경우 N의 패턴은 공백으로 채워진 가운데의 (N/3)*(N/3) 정사각형을 크기 N/3 패턴이 둘러싼 형태.

입력
3의 k승 제공
k는 1이상 8이하

출력
별 출력
'''
import sys
sys.setrecursionlimit(10**6)

def star2(num):
    if num == 1:
        return['*']
    S = star2(num//3)
    L = []

    for i in S:
        L.append(S*3)
    for i in S:
        L.append(S+' '*(num//3)+S)
    for i in S:
        L.append(S*3)
    return L

def star(num):
    global n
    if num == 3:
        g[0], g[2] = ['*', '*', '*'], ['*', '*', '*']
        g[1] = ['*', ' ', '*']
        return
    
    star(num//3)
    
    for i in range(0, num, num//3):
        for j in range(0, num, num//3):
            for k in range(num//3):
                print(g)
                if i != num//3 or j != num//3:
                    g[i+k][j:j+num//3] = g[k][:num//3]


n = int(input())
g = [[' '] * n for _ in range(n)]
star(n)
'''
for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print()
'''
