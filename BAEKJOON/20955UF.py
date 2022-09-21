'''
민서의 응급 수술


하나의 트리 형태로 연결 하려 한다. 사이클이 존재하지 않는 연결 그래프.
연결되지 않는 두 뉴런 연결 / 이미 연결 된 뉴런 간 연결 끊기.
뉴런의 연결 정보다 주어졌을 때, 모든 뉴런을 하나의 트리 형태로 연결하기 위하여 필요한 최소 연산 횟수.

입력
뉴런 갯수 n, 시냅스 갯수 m
연결 된 두 뉴런 번호 u, v 제시.

출력
트리 형태로 연결하기 위한 최소 연산 횟수
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().rstrip().split())
parent = list(range(n+1))
cnt = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    a, b = find(a), find(b)
    if a==b:
        continue
    union(a, b)
    cnt[find(a)] += cnt[find(b)]+1

a = -1
for i in range(1, n+1):
    if find(i) == i:
        a += 1
ans = (m+a) - (n-1) + a

print(ans)




'''
# 빠른 코드
import sys


sys.setrecursionlimit(int(1e5+500))


def input():
    return sys.stdin.readline().rstrip()


def main():
    def find_root(x: int) -> int:
        if roots[x] == x:
            return x
        roots[x] = find_root(roots[x])
        return roots[x]

    def union(a: int, b: int):
        if a > b:
            a, b = b, a
        roots[b] = a

    n, m = map(int, input().split())
    roots = [node for node in range(n + 1)]
    cnt_cut = 0
    for edge in range(m):
        u, v = map(int, input().split())
        root_u = find_root(u)
        root_v = find_root(v)
        if root_u != root_v:
            union(root_u, root_v)
        else:
            cnt_cut += 1
    cnt_join = len(set([find_root(node) for node in range(1, n + 1)])) - 1
    print(cnt_cut + cnt_join)


if __name__ == '__main__':
    main()
'''



