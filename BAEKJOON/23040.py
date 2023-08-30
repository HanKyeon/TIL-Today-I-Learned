'''
누텔라 트리

정점 n개 트리. 검은색 기준으로 빨간색으로 얼마나 뻗어나갈 수 있는지

입력
n 제시 10만이하
n-1개 줄 정점 번호 공백 제시
B R로 이뤄진 n길이 문자열 제시.
'''
import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y: return
    if x > y: parent[x] = y; cnt[y]+=cnt[x]
    else: parent[y] = x; cnt[x]+=cnt[y]

n = int(input())
parent, cnt = list(range(n+1)), [1]*(n+1)
queries = [list(map(int, input().rstrip().split())) for _ in range(n-1)]
s = input().rstrip()
blacks = set()
for i, v in enumerate(s):
    if v == 'B': blacks.add(i+1)
if len(blacks) == n: print(0); exit()
redRoot = []
while queries:
    a, b = queries.pop()
    if a in blacks and b in blacks: continue
    if a in blacks: redRoot.append(b); continue
    if b in blacks: redRoot.append(a); continue
    union(a, b)
ans = 0
while redRoot: ans += cnt[find(redRoot.pop())]
print(ans)

'''
# 빠른 코드; 사실 내가 젤 빠름ㅎ

"""Solution code for "BOJ 23040. 누텔라 트리 (Easy)".

- Problem link: https://www.acmicpc.net/problem/23040
- Solution link: http://www.teferi.net/ps/problems/boj/23040

Tags: [DisjointSet]

(This code was generated by Import Inliner v0.3)
"""

import sys


# >>>[BEGIN] teflib.disjointset.DisjointSet [v2.0] (Copied from teflib/disjointset.py)<<<
class DisjointSet:
    """Disjoint Set for integers with path compression and union-by-size."""

    def __init__(self, size: int):
        self._parent = [-1] * size

    def union(self, x: int, y: int, should_raise: bool = False) -> int:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            if should_raise:
                raise ValueError(f'{x} and {y} are already in the same set.')
            else:
                return root_x
        if self._parent[root_x] > self._parent[root_y]:
            root_x, root_y = root_y, root_x
        self._parent[root_x] += self._parent[root_y]
        self._parent[root_y] = root_x
        return root_x

    def find(self, x: int) -> int:
        while (p := self._parent[x]) >= 0:
            x, self._parent[x] = p, self._parent[p]
        return x

    def size(self, x: int) -> int:
        return -self._parent[self.find(x)]
# >>>[END] teflib.disjointset.DisjointSet [v2.0]<<<


def main():
    N = int(sys.stdin.readline())
    edges = [sys.stdin.readline() for _ in range(N - 1)]
    color = sys.stdin.readline()

    dsu = DisjointSet(N)
    red_groups = []
    for edge in edges:
        u, v = [int(x) for x in edge.split()]
        if color[u - 1] == color[v - 1] == 'R':
            dsu.union(u - 1, v - 1)
        elif color[u - 1] == 'R':
            red_groups.append(u - 1)
        elif color[v - 1] == 'R':
            red_groups.append(v - 1)

    print(sum(dsu.size(x) for x in red_groups))


if __name__ == '__main__':
    main()

'''
