'''
일감호에 다리 놓기

강의동은 일감호의 둘레에 따라 원형 배치. 강의동 양 옆 강의동은 서로 이웃한다. 원형 배치라서 n번째와 1번째는 이웃한다.
와우도라는 섬이 있다. k개의 돌로 징검다리 완성 가능?

입력
강의동 수 n, 공사구간 수 m, 돌 k개. 1동부터 n동까지 존재.
강의동에서 와우도까지 놓아야 하는 돌의 갯수 s1,2,3...n이 주어진다. T번째 강의동에서 와우도까지 St개의 돌을 놓아야 한다.
m개줄에 i, j 제시. i번째 강의동에서 j번째 강의동 까지 가는 길이 공사중. 이 때 입력되는 i, j 번째 건물은 이웃한 강의동이다. 공사중인 구역은 1회만 제시.

출력
가지고 있는 돌을 놓아 모든 강의동을 연결 할 수 있으면 YES, 그렇지 않으면 NO 출력.

'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        # towow[parent[x]] = min(towow[x], towow[parent[x]])
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return
    elif rx < ry:
        parent[ry] = rx
        towow[rx] = min(towow[ry], towow[rx], towow[x], towow[y])
    else:
        parent[rx] = ry
        towow[ry] = min(towow[ry], towow[rx], towow[x], towow[y])

n, m, k = map(int, input().rstrip().split())
towow = [0]+list(map(int, input().rstrip().split()))
parent = list(range(n+1))
gsz = []
fla = True
for _ in range(m):
    i, j = map(int, input().rstrip().split())
    if i > j:
        i, j = j, i
    if i == 1 and j == n:
        fla = False
        continue
    gsz.append((i, j))
if m <= 1:
    print('YES')
else:
    gsz.sort()
    if fla:
        union(1, n)
    ptr = 1

    for sta, end in gsz:
        while ptr+1<=sta:
            union(ptr, ptr+1)
            ptr += 1
        ptr = end
    while ptr+1 <= n:
        union(ptr, ptr+1)
        ptr += 1
    ans = 0
    for i in range(1, n+1):
        if parent[i] == i:
            ans += towow[i]

    # print(parent)
    # print(towow)

    if ans <= k:
        print('YES')
    else:
        print('NO')


'''
# 고수의 코드
import sys

n, m, k = map(int, sys.stdin.readline().split())
cost = list(map(int, sys.stdin.readline().split()))
disconnect = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        a, b = b, a
    if (a, b) == (1, n):
        disconnect[n] = 1
    else:
        disconnect[a] = 1

if m <= 1:
    print('YES')
    exit()

res = 0
temp = sys.maxsize
for i in range(1, n + 1):
    temp = min(temp, cost[i - 1])
    if disconnect[i]:
        res += temp
        temp = sys.maxsize

if disconnect[n] == 0:
    temp1 = sys.maxsize
    for i in range(1, n + 1):
        temp1 = min(temp1, cost[i - 1])
        temp = min(temp, cost[i - 1])
        if disconnect[i]:
            res += temp - temp1
            break

print(['NO', 'YES'][res <= k])
'''















