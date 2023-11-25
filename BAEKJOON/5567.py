'''
결혼식

상근이는 자신의 결혼식에 학교 동기 중 친구와 친구친구 초대할 것.
동기는 n명, 1부터 n까지 번호. 상근이 1번
상근이 친구 관계 리스트 있음. 결혼식에 초대할 사람 수 구해라.

입력
동기 수 n 제시
m 제시
m개 줄 친구 관계 a, b 제시

출력
초대하는 동기 수 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = int(input()), int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)
v = [0]*(n+1); v[1] =1
q, ans = deque([(1, 2)]), 0
while q:
    num, cnt = q.popleft()
    for i in g[num]:
        if v[i]: continue
        if cnt: q.append((i, cnt-1)); v[i] = 1; ans += 1
print(ans)