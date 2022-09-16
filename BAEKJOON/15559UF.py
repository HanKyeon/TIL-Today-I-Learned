'''
내 선물을 받아줘

N W E S 이동. 상 좌 우 하
이동 위치 관계 없이 선물 주는 방법. 최소 몇 칸 위에 선물을 놓아야 항상 선물을 가져가는지 구해라.

입력
지도 세로 크기 n, 가로 m 1000이하
지도 제시
지도탈출 안함

출력
최소 몇 칸에 선물을 놓아야 하는가?
'''
import sys
input = sys.stdin.readline

def find(x):
    # x를 받아서 x의 루트를 반환하는 함수.
    if parent[x] != x:
        parent[x] = find(parent[x])
    sets.add(parent[x])
    return parent[x]

def union(x, y):
    # x, y를 받아서 두 노드를 합치는 함수. 더 작은 값으로 따라간다.
    a, b = find(x), find(y)
    if a==b:
        return
    if a < b:
        parent[b] = a
        if b in sets:
            sets.remove(b)
        return
    elif b < a:
        parent[a] = b
        if a in sets:
            sets.remove(a)
        return

di = {'N':(-1, 0), 'W':(0, -1), 'E':(0, 1), 'S':(1, 0)}

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
parent = list(range(n*m))
sets = set()
for i in range(n):
    for j in range(m):
        dh, dw = di[g[i][j]]
        ni, nj = i+dh, j+dw
        union(i*m+j, ni*m+nj)
print(len(sets))
























