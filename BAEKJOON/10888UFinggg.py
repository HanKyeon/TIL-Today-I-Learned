'''
두 섬간의 이동

1에서 n까지의 섬 일렬로.
다리 지을 예정.
섬 i와 i+1을 연결하는 다리 총 n-1개 지을 계획. 짓는 순서에 따라 몇개가 달라진다. 지어질 때 마다

두 섬 간에 왕래가 가능한 섬들 쌍의 갯수.
두 섬 i, j가 왕래 가능 할 때 섬i에서 섬 j까지 가기 위해 이용해야 하는 최소 다리 갯수의 합.

두 값을 구해야 한다.

입력
섬의 갯수 n 제시.
n-1개 줄에 정수 i 제시. i와 i+1을 잇는 다리를 짓겠다는 의미. 중복해서 등장하는 수는 없다.

출력
다리를 지을 때마다 두 섬 간에 왕래가 가능한 섬들 쌍의 갯수, 두 섬까지 가기 위한 최소 다리 갯수의 합.
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find해서 넣기
    x, y = find(x), find(y)
    parent[y] = x
    nodc[x] += nodc[y]
    if x not in grp:
        grp.add(x)
    if y in grp:
        grp.remove(y)

n = int(input())
parent = list(range(n+1))
nodc = [1]*(n+1)
memo1, memo2 = [0]*(n+1), [0]*(n+1)
memo1[2], memo2[2] = 1, 1
for i in range(3, n+1):
    memo1[i] = memo1[i-1] + i-1
    memo2[i] = memo2[i-1] + memo1[i]

grp = set()
for _ in range(n-1):
    a = int(input())
    union(a, a+1)
    ans1, ans2 = 0, 0
    for i in grp:
        a = nodc[i]
        ans1 += memo1[a]
        ans2 += memo2[a]
    print(ans1, ans2)










