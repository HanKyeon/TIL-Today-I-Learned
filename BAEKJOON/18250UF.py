'''
철도 여행

n개 도시, m개 철도.
하나의 철도 노선을 두 번 이상 타지 않을 것. 시작 도착은 같을 수도 있고, 하나 도시 다중 방문 가능. 노선만 1회.
최소 철도 여행으로 모든 노선 한 번씩 탈 것. 철도 여행 몇 번 해야함?

입력
첫 줄에 두 정수 n, m 제시.
m개 줄에 걸쳐 u, v 제시. u-v 간 노선 존재. 두 개의 도시를 직접 잇는 철도 노선은 1개

출력
철도 여행 최소 횟수
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서
    a, b = find(x), find(y)
    if a==b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().rstrip().split())
parent = list(range(n+1))
edges = [0] * (n+1)
grpegs = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    edges[a]+=1
    edges[b]+=1
    union(a, b)
for i in range(1, n+1):
    grpegs[find(i)].append(edges[i])

# print(parent)
# print(edges)
# print(grpegs)
ans = 0
for i in grpegs:
    # if not i:
    #     continue
    if len(i) <= 1:
        continue
    if len(i) == 2:
        ans += 1
        continue
    cnt = 0
    for j in i:
        if j % 2:
            cnt += 1
    if cnt==0: #  or cnt==2
        ans+=1
        continue
    else:
        ans += cnt//2

print(ans)






'''
알 수 없는게 많이 쓰인 약간 빠른 코드

import os
import sys
from io import BytesIO, IOBase


def main():
    n,m = map(int,input().split())
    graph = []
    for _ in range(n):
        graph.append([])
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    def connected_components(n, graph):
        components, visited = [], [False] * n

        def dfs(start):
            component, stack = [], [start]

            while stack:
                start = stack[-1]

                if visited[start]:
                    stack.pop()
                    continue
                else:
                    visited[start] = True
                    component.append(start)

                for i in graph[start]:
                    if not visited[i]:
                        stack.append(i)

            return component

        for i in range(n):
            if not visited[i]:
                components.append(dfs(i))

        return components

    c = connected_components(n, graph)
    ans = 0
    for component in c:
        if len(component) == 1:
            continue
        tmp = 0
        for elem in component:
            tmp += len(graph[elem]) % 2
        ans += max(1, tmp // 2)
    print(ans)

# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
'''