'''
n과 m 3

1부터 n까지 자연수 중 m개를 고른 수열.
같은 수를 여러번 골라도 됨.

입력
n, m 제시.

출력
다 출력
'''
n, m = map(int, input().rstrip().split())
nl = []
def dfs(cnt):
    if not cnt:
        print(*nl)
        return
    for i in range(1, n+1):
        nl.append(i)
        dfs(cnt-1)
        nl.pop()
dfs(m)


'''
from itertools import product

n, m = map(int, input().split())

print("\n".join(list(map(" ".join, product([str(i) for i in range(1, n + 1)], repeat = m)))))
'''
