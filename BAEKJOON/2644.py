'''
촌수계산

촌수 계산

입력
n 제시
두 번호 제시
관계 갯수 m 제시 a, b일 때 a가 b의 부모이다.
간선 제시.

출력
촌수 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s, e = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)
v = [0]*(n+1)
q = deque([s])
v[s] = 1
while q:
    num = q.popleft()
    for i in g[num]:
        if v[i]:
            continue
        v[i] = v[num]+1
        q.append(i)
    if v[e]:
        break
print(v[e]-1)


