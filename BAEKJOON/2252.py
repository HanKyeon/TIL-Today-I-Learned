'''
줄 세우기

N명의 학생을 키 순서로 세우려고 함.
일부 학생의 키만 비교해봄.

입력
1이상 32000이하 N, 1이상10만이하 M 제시 M은 키 비교 횟수
앞이 작고 뒤가 크다. 번호는 1~N

출력
학생들을 앞에서부터 줄을 세운 결과 출력
'''

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
reqk = [0] * (n+1)
# v = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    reqk[b] += 1

q = deque()
for i in range(1, n+1):
    if reqk[i] == 0:
        q.append(i)

while q:
    nn = q.popleft()
    # if v[nn] == 1:
        # continue
    # v[nn] = 1
    print(nn, end=' ')
    for i in g[nn]:
        reqk[i] -= 1
        if reqk[i] == 0:
            q.append(i)





