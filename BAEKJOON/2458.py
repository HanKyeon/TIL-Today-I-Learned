'''
키 순서

1부터 n까지 학생의 키를 비교한 결과의 일부 제시. n명의 키는 모두 다르다.

입력
학생의 수 2이상 500이하 n, 비교 횟수 m 제시 0이상 n(n-1)/2 이하
키 비교 결과 a, b. a인 학생이 번호가 b인 학생보다 작다.

출력
자신이 키가 몇 번째인지 알 수 잇는 학생의 수
'''
from collections import deque
import sys
input = sys.stdin.readline

def ts(sta):
    global n
    v = [0]*(n+1)
    b, s = 0, 0
    bq, sq = deque([sta]), deque([sta])
    v[sta] = 1
    while bq:
        nn = bq.popleft()
        b += 1
        for i in bgr[nn]:
            if v[i] == 0:
                v[i] = 1
                bq.append(i)
    while sq:
        nn = sq.popleft()
        s += 1
        for i in smr[nn]:
            if v[i] == 0:
                v[i] = 1
                sq.append(i)
    return b+s-1


n, m = map(int, input().split())
bgr = [[] for _ in range(n+1)]
smr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    bgr[a].append(b) # a가 작다
    smr[b].append(a) # b가 크다
ans = 0
for i in range(1, n+1):
    if ts(i) == n: # 반환값이 n명이라면
        ans += 1

print(ans)
