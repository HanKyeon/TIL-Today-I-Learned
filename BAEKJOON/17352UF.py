'''
요로분의 다리가 되어 두리겠스므니다.

n개 섬. 1~n 번호.
n-1개 다리. 어떤 두 섬이든 다리 왕복 가능.
욱제가 다리 하나 박살.

첫 줄에 정수 N 제시.
다음 N-2개의 줄에 욱제가 무너뜨리지 않는 다리를 잇는 두 섬의 번호 제시.

출력
다리로 이을 두 섬의 번호 출력. 여러 방법이 있을 경우 그 중 아무ㅏ거나 출력.
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x==y:return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
parent = [i for i in range(n+1)]
for _ in range(n-2):
    a, b = map(int, input().rstrip().split())
    union(a, b)
ans = []
for i in range(1, n+1):
    if parent[i] == i:
        ans.append(i)
    if len(ans) == 2:
        break
print(*ans)







