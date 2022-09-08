'''
장난감 조립
장난감에는 기본 부품, 중간붚무이 사용.
기본 부품은 조립될 수 없음.
중간 부품은 중간+기본으로 만들어짐.
완제품과 그에 필요한 부품들 사이 관계 제시. 하나의 완제를 조립하기 위해 필요한 기본 부품의 종류 별 갯수 계산.

입력
3이상 100이하 n 1부터 n-1까지는 기본부품, 중간부품 번호, n은 완제품
3이상 100이하 m
m개 줄에 부품 관계. x, y, k.
x를 만드는데 중간 혹은 기본 y가 k개 필요하다는 뜻. 두 중간 부품이 서로를 필요로 하는 경우x

출력
하나의 완제품을 조립하는데 필요한 기본 부품의 수를 한 줄에 하나씩 출력. 중간부품x 반드시 기본 부품의 번호가 작은 것부터 큰 순서가 되도록. 각 줄에는 기본 부품의 번호와 소요 갯수 출력
'''
'''
기본 부품과 중간 부품을 판별해야 함. -> 레시피가 있느냐 없느냐로 판별해야 할 듯.
뻗어나간 최종 아랫 바닥을 가면 될듯.
혹은 0부터 n까지 갯수를 만들고 해도 될듯....하다만
'''
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
needed = [[0 for _ in range(n+1)] for _ in range(n+1)]
basics = []

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().rstrip().split())
    nodes[y].append([x, k])
    in_degree[x] += 1

queue = deque()

for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)
        basics.append(i)
        # degree 값이 0인 노드는 기본 부품

while queue:
    cur_node = queue.popleft()
    for next_node, next_cost in nodes[cur_node]:
        if cur_node in basics:
            needed[next_node][cur_node] += next_cost
        else:
            for i in range(1, n+1):
                needed[next_node][i] += needed[cur_node][i] * next_cost
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

for num, cnt in enumerate(needed[n][1:], start=1):
    if cnt > 0:
        print(num, cnt)
for i in needed:
    print(i)

'''
# 빠른 코드

# 08.17
# https://www.acmicpc.net/problem/2637
# 접근 방법
# 각 부품마다 기본 부품이 몇 개 필요한지를 리스트 형태로 만든 뒤 dfs를 통해 부품을 탐색한다. 
# 이때 dp 테이블을 만들어 필요한 기본 부품의 개수를 저장해 반복적인 작업을 없앤다.
import sys
input = sys.stdin.readline

def dfs(now):
    if visited[now]:
        return dp[now]
    
    for i in range(1, n+1):
        if not graph[now][i]: continue
        need_cnt = graph[now][i]
        temp = dfs(i)
        for pp in primary_part:
            dp[now][pp] += temp[pp] * need_cnt
    
    visited[now] = True
    return dp[now]

n, m = int(input()), int(input())
indegree = [0 for _ in range(n+1)]
graph = [[0 for _ in range(n+1)] for _ in range(n+1)] # 각 부품별 필요한 기본 부품의 개수를 저장할 리스트

# 각 부품을 만들기 위해 필요한 부품 체크
for _ in range(m):
    x, y, k = map(int, input().split())
    indegree[x] += 1
    graph[x][y] = k

# 기본 부품 정리
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
primary_part = []
for i in range(1, n+1):
    if not indegree[i]: primary_part.append(i)
    
for x in primary_part:
    dp[x][x] = 1
    visited[x] = True

dfs(n)
for x in primary_part:
    print(x, dp[n][x])

'''


'''
# 시간 메모리 전부 초과
from collections import deque
import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
rcp = [[] for _ in range(m)] # 레시피
howmany = [0]*(n)+[1] # n에서 뻗어나갈 것이다.
middle = {0, n}
for i in range(m):
    x, y, k = map(int, input().rstrip().split())
    middle.add(x)
    rcp[x].append((y, k)) # 레시피. x를 만들려면 y가 k개 필요하다.

q = deque([n]) # n을 1개 만들거다.
while q:
    mk = q.popleft() # mk를 mknum개 만들 거다
    if not mk in middle:
        continue
    for i in rcp[mk]: # mk의 레시피를 보면서
        req, reqnum = i # 요구 부품 번호, 요구 갯수
        howmany[req] += reqnum*howmany[mk] # 갯수에 갱신해준다. 요구 갯수를 mknum개 만큼 만들어야 한다.
        q.append(req) # 요구되는 것
    howmany[mk] = 0
    # print(howmany)
for i in range(1, n+1):
    if not i in middle:
        print(i, howmany[i])
'''


'''
# 메모리 초과 bfs

from collections import deque
import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
rcp = [[] for _ in range(m)] # 레시피
howmany = [0]*(n+1) # n에서 뻗어나갈 것이다.
middle = {0, n}
for i in range(m):
    x, y, k = map(int, input().rstrip().split())
    middle.add(x)
    rcp[x].append((y, k)) # 레시피. x를 만들려면 y가 k개 필요하다.

q = deque([(n, 1)]) # n을 1개 만들거다.
while q:
    mk, mknum = q.popleft() # mk를 mknum개 만들 거다
    for i in rcp[mk]: # mk의 레시피를 보면서
        req, reqnum = i # 요구 부품 번호, 요구 갯수
        if req not in middle: # 중간 부품이 아니라면
            howmany[req] += reqnum*mknum # 갯수에 갱신해준다. 요구 갯수를 mknum개 만큼 만들어야 한다.
            continue # 다음!
        q.append((req, reqnum*mknum)) # 요구되는 것, 요구되는 개수 * 만들어야 할 갯수

for i in range(1, n+1):
    if not i in middle:
        print(i, howmany[i])

'''














