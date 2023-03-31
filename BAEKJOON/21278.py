'''
호석이 두마리 치킨

n개 도시 m개 도로. 1부터 n. i번ㅉ ㅐ도로는 ai bi를 1시간에 양방향 이동 가능.
2개 건물 골라서 치킨집 열 것. 건물에서 접근성 합 최소화. x의 접근성은 x에 가장 가까운 호석이 두마리 치킨집까지 왕복하는 최단시간.
모든 건물에서 가장 가까운 치킨 집까지 왕복하는 최단 시간의 총합을 최소화 할 수 있는 건물 2개의 번호와 그 때의 모든 건물에서 가장 가까운 치킨집까지 왕복하는 최단 시간의 총합을 출력하라. 건물 번호 중 작은게 더 작을 수록, 작은 번호가 같다면 큰 번호가 더 작을수록 좋은 건물 조합.

입력
n, m 제시.
m개 줄 도로 정보 a, b 제시.

출력
건물 2개가 지어질 건물 번호를 오름차순 출력, 그 때 모든 도시에서의 왕복 시간의 합 출력.
조합이 많다면 작은 번호가 더 작은 것을, 작은 번호가 같다면 큰 번호가 더 작은걸 출력.
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(idx):
    global n
    v = [0]*(n+1)
    v[idx] = 1
    q = deque([idx])
    while q:
        num = q.popleft()
        for i in g[num]:
            if v[i]:
                continue
            v[i] = v[num]+1
            q.append(i)
    v = [i-1 if i else i for i in v]
    return v

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)

bfsz = []
for i in range(1, n+1):
    bfsz.append(bfs(i))
ans = int(10e9)
idx1, idx2 = 0, 0
for i in range(n-1):
    for j in range(i+1, n):
        a = sum([min(a) for a in zip(bfsz[i], bfsz[j])]) * 2
        if ans > a:
            ans = a
            idx1, idx2 = i+1, j+1
print(idx1, idx2, ans)









