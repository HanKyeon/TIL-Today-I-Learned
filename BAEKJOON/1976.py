'''
여행 가자

도시 N개.
슈뢰딩거의 길
여행 일정 줬을 때 여행 경로가 가능한가?
다른 도시 경유 가능.
도시와 도시 간 연결 여부 제시, 여행 계획에 속한 도시들이 제시. 가능한지? 중첩 방문 ㅆㄱㄴ

입력
200 이하 n
여행 계획에 속한 도시 수 1000이하 m
그래프 제시.
g[i][j]가 1이라면 연결, 아니라면 연결 안됨.
A B 연결 시 B A 연결.
여행 계획.(방문 예정 도시들 제시.)

출력
가능하면 YES 불가능이면 NO
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a == b: return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def check(li):
    global nl
    cc = find(li[0]-1)
    fla = False
    for i in nl:
        if find(i-1) != cc:
            fla = True
    if fla:
        print('NO')
    else:
        print('YES')

n, m = int(input()), int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
nl = list(map(int, input().rstrip().split()))
parent = list(range(n))
for i in range(n):
    for j in range(i, n):
        if g[i][j]:
            union(i, j)
check(nl)
























