'''
카드 게임

1. N개의 빨간색 카드가 있다. 각각의 카드는 순서대로 1부터 N까지 번호가 매겨져 있다. 이 중에서 M개의 카드를 고른다.
2. N개의 파란색 카드가 있다. 각각의 카드는 순서대로 1부터 N까지 번호가 매겨져 있다. 이 중에서 빨간색에서 고른 번호와 같은 파란색 카드 M개를 고른다.
3. 철수는 빨간색 카드를 가지고 민수는 파란색 카드를 가진다.
4. 철수와 민수는 고른 카드 중에 1장을 뒤집어진 상태로 낸다. 그리고 카드를 다시 뒤집어서 번호가 큰 사람이 이긴다. 이 동작을 K번 해서 더 많이 이긴 사람이 최종적으로 승리한다. 한 번 낸 카드는 반드시 버려야 한다.

철수는 사기꾼이라 조작 가능. 카드를 버리고 몰래 다시 들고 오거나, 민수한테 없는 카드도 낸다.
민수는 심리학자라 미래를 알 수 있음. 철수가 낼 카드보다 큰 카드가 있다면 그 카드들 중 가장 작은 카드를 낼 것.

K번 동안 철수가 낼 카드가 입력으로 제시. 민수는 어떤 카드를 내는가? 민수가 카드 못내는 경우는 없다.

입력
n, m, k 제시. 1<=m<=n<=400만 1이상 m이하 k 최대 만
카드 번호 m개 자연수. 1이상 n이하 서로 다름.
k개의 자연수 제시. i번째 수는 철수가 i번째로 내는 카드 번호. 철수 카드 역시 1이상 n이하.

출력
k줄에 걸쳐 수를 출력. i번째 줄에는 민수가 i번째로 낼 카드의 번호 출력
'''
import sys
input = sys.stdin.readline
print = sys.stdout.write

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 안하고 넣을 것.
    a, b = find(x), find(y)
    if a == b:
        return
    if a > b:
        parent[b] = a
        print(str(nl[b])+'\n')
    else:
        parent[a] = b
        print(str(nl[a])+'\n')

def bs(tg):
    global m
    sta, end = 0, m-1
    ret =int(4000001)
    mid = (sta+end)//2
    while sta <= end:
        mid = (sta+end)//2
        # print(mid, sta, end)
        if nl[mid] <= tg:
            sta = mid+1
        elif nl[mid] > tg:
            ret = min(mid, ret)
            end = mid-1
    return ret


n, m, k = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))
cs = list(map(int, input().rstrip().split()))
parent = list(range(m+1))
nl = sorted(nl) + [4000005]

# print(nl)
# print(bs(2))
# print(bs(3))
# print(bs(4))
# print(bs(5))
# print(bs(7))
# print(bs(8))
# print(bs(9))

for i in cs:
    j = bs(i)
    a = find(j)
    union(a, a+1)







'''
# 시간 초과
import sys
input = sys.stdin.readline
# print = sys.stdout.write

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 안하고 넣을 것.
    a, b = find(x), find(y)
    if a == b:
        return
    if a > b:
        parent[b] = a
        print(nl[b])
    else:
        parent[a] = b
        print(nl[a])

n, m, k = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))
cs = list(map(int, input().rstrip().split()))
parent = list(range(m+1))
nl = sorted(nl) + [int(10e9)]
# print(parent)
# print(nl)
for i in cs:
    for j in range(n):
        if nl[j] > i:
            a = find(j)
            union(a, a+1)
            # print(nl[j])
            break
# print(parent)
# print(nl)
'''













