'''
엘리베이터

n층 아파트, m대 엘베. 엘베는 1부터 m까지 번호.
엘베 특정 층만 멈춤. i번 엘베는 xi번쨰 층에서 시작하여 yi번째 층에서만 선다. 4, 3이라면 4, 7, 10 층.
A층 사는 철수 B층 사는 친구네 놀러 가려 한다. 가능한 엘베 적게 타고.

입력
n, m 제시.
m개 줄 xi, yi 제시.
a, b 제시.
n은 10만이하, m은 100이하 자연수
x, y, a, b는 모두 n 이하 자연수. a, b는 서로 다름

출력
A에서 B로 가기 위해 최소 몇 번 엘베 타야 하는가?
타야하는 엘베 번호 한 줄에 하나씩 순서대로 출력.
못가면 -1 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

def lego():
    """거꾸로 레고~"""
    global n, m, a, b
    v = [[] for _ in range(n+1)]
    v[b] = [0]
    q = deque([b])
    while q:
        flr = q.popleft()
        for en in g[flr]:
            for nflr in ev[en]:
                if v[nflr]:
                    continue
                v[nflr] = v[flr][:]
                v[nflr].append(en)
                q.append(nflr)
                if nflr == a:
                    return v[nflr]
    return []

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
ev = [[] for _ in range(m+1)]
for i in range(1, m+1):
    x, y = map(int, input().rstrip().split())
    k = 0
    xyk = x+y*k
    while xyk <= n:
        g[xyk].append(i)
        ev[i].append(xyk)
        k+=1
        xyk = x+y*k

a, b = map(int, input().rstrip().split())
ans = lego()
if not ans:
    print(-1)
    exit()
ans.pop(0)
print(len(ans))
for i in reversed(ans):
    print(i)

'''
# real super fast

def einvmod(a, b):
    oa, ob = a, b
    aa = 1
    ab = 0
    while b:
        q = a // b
        a, b = b, a % b
        ar = aa - ab * q
        aa, ab = ab, ar
    return aa % ob, a

def adj(p1, p2, lim):
    s1, t1 = p1
    s2, t2 = p2
    a1 = s1 % t1
    a2 = s2 % t2
    v, g = einvmod(t1, t2)
    if (a1 - a2) % g != 0:
        return False
    a = a1 + (a2 - a1) * v % t2 * (t1 // g)
    t = t1 // g * t2
    assert a % t1 == a1 and a % t2 == a2 and 0 <= a < t
    return ((max(s1, s2) - a - 1) // t + 1) * t + a <= lim


def adjv(v, p):
    s, t = p
    return v >= s and (v - s) % t == 0


MII = lambda: map(int, input().split())
n, m = MII()
tr = [[] for __ in range(m + 2)]

def add_edge(u, v):
    tr[u].append(v)
    tr[v].append(u)

ps = [tuple(MII()) for __ in range(m)]
vs, ve = MII()
for i, p in enumerate(ps, 1):
    if adjv(vs, p):
        add_edge(i, 0)
    if adjv(ve, p):
        add_edge(i, m + 1)
for i, pi in enumerate(ps, 1):
    for j, pj in enumerate(ps, 1):
        if j >= i: break
        if adj(pi, pj, n):
            add_edge(i, j)


visited = [None] * (m + 2)
visited[0] = -1
q = [0]

for u in q:
    for v in tr[u]:
        if visited[v] is not None:
            continue
        visited[v] = u
        q.append(v)


if visited[-1] is None:
    print(-1)
else:
    a = []
    v = -1
    while visited[v] != -1:
        a.append(v)
        v = visited[v]
    a.reverse()
    a.pop()
    print(len(a))
    for v in a:
        print(v)
'''
