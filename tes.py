'''
한 작품이 다른 작품과 비교하여 세가지 심사 포인트 점수가 같거나 큰 경우 다른 작품이 떨어짐.
n개의 출품작들의 세가지 점 수 제시, 작품상을 수상하는 작품의 최소 갯수.

입력
작품수 n 제시
점수 a,b,c 제시
'''
import sys
input = sys.stdin.readline

def matching(idx):
    for i in g[idx]:
        if v[i]: continue
        v[i] = 1
        if connect[i] < 0 or matching(connect[i]):
            connect[i] = idx
            return True
    return False

def check(idx1, idx2):
    art1, popular1, scenario1 = nl[idx1]
    art2, popular2, scenario2 = nl[idx2]
    hasSame0, hasSame1, hasSame2 = art1 == art2, popular1 == popular2, scenario1 == scenario2
    if hasSame0 and hasSame1 and hasSame2:
        g[idx1].append(idx2)
        g[idx2].append(idx1)
        return
    big0, big1, big2 = art1 >= art2, popular1 >= popular2, scenario1 >= scenario2
    if big0 and big1 and big2:
        g[idx1].append(idx2)
    elif not big0 and not big1 and not big2:
        g[idx2].append(idx1)

n = int(input())
nl = [list(map(int, input().rstrip().split())) for _ in range(n)]
g = [[] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        check(i, j)
connect = [-1]*n
ans, flag = n, True
for _ in range(2):
    for i in range(n):
        v = [0]*n
        if matching(i):
            ans -= 1
print(ans)

'''
3
15 54 35
12 12 15
18 38 34

2

5
26 13 29
16 2 24
14 23 4
17 1 10
7 25 8

3
'''
