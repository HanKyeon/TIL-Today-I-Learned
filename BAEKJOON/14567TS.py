'''
선수과목

어떤 과목들은 선수과목이 있어 해당되는 모든 과목을 먼저 이수해야만 해당 과목을 이수 할 수 있게 되어 잇다.
1. 한 학기에 들을 수 있는 과목 수 제한 x
2. 모든 과목은 매 학기 항상 개성
모든 과목에 대해 각 과목을 이수하려면 최소 몇 학기가 걸리는가?

입력
과목의 수n, 선수 조건의 수 m 제시.
m개 줄 a, b. a번 과목이 b 과목의 선수 과목이다. a<b 입력만 제시.

출력
1번 과목부터 n번 과목까지 차례대로 최소 몇 학기에 이수 할 수 있는지 한 줄에 공백 구분 출력.
'''
from collections import deque
import sys
input = sys.stdin.readline

def ts(idx):
    q = deque()
    for i in range(1, n+1):
        if not reqn[i] and not ans[i]:
            q.append(i)
    if not q:
        return False
    while q:
        num = q.popleft()
        ans[num] = idx
        for i in g[num]:
            reqn[i] -= 1
    return True

n, m = map(int, input().rstrip().split())
reqn = [0] * (n+1)
g = [[] for _ in range(n+1)]
ans = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    reqn[b] += 1

a = ts(1)
i = 2
while a:
    a = ts(i)
    i += 1
print(*ans[1:])
























