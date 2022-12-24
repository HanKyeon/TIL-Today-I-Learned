'''
노트북의 주인을 찾아서

자신의 것 같다 얘기한 노트북을 갖는 사람 최대화.

입력
노트북 구입 사람 수 n, 노트북 예상 갯수 m
m개 줄 a, b 제시. a번 사람이 b번이 내꺼 갖다라는 뜻.
1~n 1~m이다.

출력
최대값
'''
import sys
input = sys.stdin.readline

def matching(idx):
    for i in g[idx]:
        if v[i]:
            continue
        v[i] = 1
        if not connect[i] or matching(connect[i]):
            connect[i] = idx
            return True
    return False

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)

connect = [0]*(n+1)
ans = 0
for i in range(1, n+1):
    v = [0]*(n+1)
    if matching(i):
        ans += 1
    if ans == m:
        break

print(ans)
