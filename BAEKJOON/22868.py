'''
산책

s에서 출발, e를 찍고 s로 돌아올 것.
이미 갔던 정점은 또 가기 싫어서 온 거리 제외하고 감.
산책 거리 긴 것 싫어서 둘 다 짧은걸 원한다.
S에서 E로 이동 할 때 짧은 거리 경로가 여러개 나올 수 있다. S에서 정점 E로 이동한 경로를 나열 했을 때, 사전 순으로 가장 먼저 오는 것 선택.
산책 전체 경로의 거리를 구하자.

입력
n, m 제시.
m개 줄 a, b 제시. 거리는 항상 1 양방향
s, e 제시.

출력
산책의 전체 경로 길이
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(sta, end):
    global s, e, n
    q = deque([(sta, [sta])])
    v[sta] = 0
    while q:
        num, ret = q.popleft()
        for i in g[num]:
            if i == end:
                return ret+[i]
            if v[i] > v[num]+1:
                v[i] = v[num]+1
                q.append((i, ret+[i]))


n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)
s, e = map(int, input().rstrip().split())
for i in range(1,n+1):
    g[i].sort()
v = [10001] * (n+1)
a = bfs(s, e)
ans = len(a)
v = [10001] * (n+1)
while a:
    num = a.pop()
    v[num] = 0
a = bfs(e, s)
ans += len(a)
print(ans-2)








