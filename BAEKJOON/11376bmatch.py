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
# 빠른 코드

from sys import stdin

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    # 직원에 해당하는 변수로 1인당 2개까지 일할 수 있으므로 1명을 2명으로 만들어준다
    # left_vertex[i] = [i번째 직원이 할 수 있는 일들]
    left_vertex = [0] * (N + 1)
    for i in range(1, N + 1):
        _, *works = map(int, input().split())
        left_vertex[i] = works

    ans = 0
    # 일에 해당하는 변수
    # right_vertex[i] = j --> i번째 일은 j번째 직원이 한다
    right_vertex = [0] * (M + 1)

    def bipartite_matching(visited, here):
        visited[here] = True
        for there in left_vertex[here]:
            if not right_vertex[there]:
                right_vertex[there] = here
                return True
        for there in left_vertex[here]:
            if not visited[right_vertex[there]] and right_vertex[there] != here and bipartite_matching(visited, right_vertex[there]):
                right_vertex[there] = here
                return True
        return False

    for i in range(1, N+1):
        if bipartite_matching([False]*(N+1), i):
            ans += 1
        if bipartite_matching([False]*(N+1), i):
            ans += 1
        if ans == M:
            break

    return ans


if __name__ == '__main__':
    print(solve())
'''












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
