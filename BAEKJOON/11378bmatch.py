'''
열혈강호 4

n명의 직원 m개의 해야 할 일.
각 일을 담당하는 사람은 1명
벌점 X를 받은 사람은 최대 X+1개의 일 가능
하지만 각 직원은 자신이 지난 달에 받은 벌점을 보르고 직원이 받은 벌점의 합 K만 알고 있다. 조작해서 쓸 수 있다.
직원이 할 수 있는 일의 목록과 지난 달 받은 벌점의 합 K가 제시되었을 때, M개 일 중 최대 몇개를 할 수 있는가.

입력
n, m, k 제시.
n개 줄 i번 직원이 할 수 있는 일의 갯수와 할 수 있는 일 번호 제시.

출력
할 수 있는 최대 일의 갯수
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
            return 1
    return 0

n, m, k = map(int, input().rstrip().split())
g = [[]]
for i in range(1, n+1):
    s = list(map(int, input().rstrip().split()))
    s.pop(0)
    g.append(s)
connect = [0] * (m+1)
ans, cnt = 0, 0
for i in range(1, n+1):
    v = [0]*(m+1)
    if matching(i):
        ans += 1
    if ans == m:
        break

if ans == m:
    print(ans)
    exit()

while cnt != k:
    fla = 0
    for i in range(1, n+1):
        v = [0]*(m+1)
        a = matching(i)
        fla += a
        if a:
            ans += 1
            cnt += 1
        if ans == m or cnt == k:
            break
    if not fla:
        break
    if ans == m:
        break

print(ans)

'''
import sys
input = sys.stdin.readline

def dfs(visited, i):
    visited[i] = True
    for v in graph[i]:
        if R[v] == -1:
            R[v] = i
            return True
    for v in graph[i]:
        if not visited[R[v]] and R[v] != i and dfs(visited, R[v]):
            R[v] = i
            return True
    return False


N, M, K = map(int, input().split())
graph = []
L = [0] * N
R = [-1] * M
ans, _K = 0, K
remain = set()

for i in range(N):
    _, *want = list(map(int, input().split()))
    graph.append([v - 1 for v in want])
    if graph[i]: remain.add(i)

while 1:
    prev = ans
    full = set()
    for i in remain:
        if dfs([False] * N, i):
            ans += 1
            L[i] += 1
            if L[i] >= 2: _K -= 1
            if L[i] == len(graph[i]): full.add(i)
        if ans == M or ans == N + K or _K == 0: print(ans); exit()
    if prev == ans: break
    remain -= full

print(ans)
'''
























