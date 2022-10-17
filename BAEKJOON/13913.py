'''
숨바꼭질 4

수빈이 숨바꼭질. 점N에 있고, 동생은 점 K에 있다. 수빈이는 걷거나 순간이동 할 수 있다. 수빈 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동, 순간이동은 1초 후에 2*X로 이동.
수빈이와 동생 위치 제시. 수빈이가 동생 찾을 수 있는 가장 빠른 시간이 몇 초 후인가?

입력
수빈이 위치 N, 동생 위치 K 제시.

출력
수빈이가 동생을 찾는 가장 빠른 시간 출력.
어떻게 이동해야 하는지 공백으로 구분해 출력.
'''
from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(100010)

n, m = map(int, input().rstrip().split())
def bfs():
    global n, m
    if n > m:
        return list(range(n, m-1, -1)), n-m
    elif n == m:
        return [n], 0
    v = [-1]*(m+5)
    q = deque()
    q.append(n)
    v[n] = n
    while q:
        num = q.popleft()
        if num+1 < m+5 and v[num+1] < 0:
            v[num+1] = num
            if num+1 == m:
                break
            q.append(num+1)
        if num-1 >= 0 and v[num-1] < 0:
            v[num-1] = num
            if num-1 == m:
                break
            q.append(num-1)
        if num*2<m+5 and v[num*2] < 0:
            v[num*2] = num
            if num*2 == m:
                break
            q.append(num*2)
    ret = []
    def find(x):
        ret.append(x)
        if x == n:
            return
        find(v[x])
    find(m)
    return reversed(ret), len(ret)-1
a = bfs()
print(a[1])
print(*a[0])



'''
# 빠른 코드인데 dfs를 하네..;

def dfs(n, k):
    if n >= k:
        return n - k, [i for i in range(n, k - 1, -1)]
    elif k == 1: # n == 0
        return 1, [0, 1]
    elif k % 2 == 0: # k is even
        opt, path = dfs(n, k // 2)
        if k - n <= 1 + opt:
            return k - n, [i for i in range(n, k + 1)]
        else:
            return 1 + opt, path + [k]
    else: # k is odd
        opt1, path1 = dfs(n, k + 1)
        opt2, path2 = dfs(n, k - 1)
        if opt1 <= opt2:
            return 1 + opt1, path1 + [k]
        else:
            return 1 + opt2, path2 + [k]

n, k = map(int, input().split())
opt, path = dfs(n, k)
print(opt)
print(" ".join(map(str, path)))
'''





