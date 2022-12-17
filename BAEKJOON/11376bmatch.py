'''
열혈강호2

직원 n명 해야 할 일 m개.
직원 1~n 일 1~m
각 직원은 최대 2개의 일 가능.
m개 일 중 최대 몇개 할 수 있는지?

입력
n, m  제시.
n개 줄 i번째 i번 직원이 할 수 있는 일의 갯수와 할 수 있는 일의 번호 제시.

출력
할 수 있는 일의 갯수 출력
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1111)

def matching(idx):
    for i in g[idx]:
        if v[i]:
            continue
        v[i] = 1
        if not connect[i] or matching(connect[i]):
            connect[i] = idx
            return 1
    return 0

n, m = map(int, input().rstrip().split())
g = [[]]
for _ in range(n):
    s = list(map(int, input().rstrip().split()))
    s.pop(0)
    g.append(s)
connect = [0]*(m+1)
for i in range(1, n+1):
    v = [0]*(m+1)
    matching(i)
for i in range(1, n+1):
    v = [0]*(m+1)
    matching(i)
print(m+1-connect.count(0))














'''
import sys
input = sys.stdin.readline

def check(idx):
    for i in g[idx]:
        if v[i]:
            continue
        if connect[i] == idx:
            continue
        v[i] = 1
        if not connect[i]:
            return i
    return False

def matching(idx):
    wcnt = working[idx]
    if not wcnt:
        return False
    for i in g[idx]:
        if v[i]:
            continue
        v[i] = 1
        if not connect[i]:
            connect[i] = idx
            wcnt -= 1
            if not wcnt:
                working[idx] = wcnt
                return True
            continue
        if connect[i] == idx:
            continue
        bidx = connect[i]
        a = check(bidx)
        if a:
            connect[i] = idx
            connect[a] = bidx
            matching()
    return working[idx] == 2

n, m = map(int, input().rstrip().split())
g = [[]]
for i in range(n):
    s = list(map(int, input().rstrip().split()))
    s.pop(0)
    g.append(s)
connect = [0]*(m+1)
working = [2]*(n+1)
for i in range(1, n+1):
    v = [0] * (m+1)
    matching(i)

print(m+1-connect.count(0))
'''
