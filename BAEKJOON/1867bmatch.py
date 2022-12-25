'''
돌멩이 제거

n행 n열 격자 운동장.
k개의 돌멩이. 한 칸당 하나
돌멩이를 제거 할 때는 한 행이나 열을 직선으로 달려가면서 그 행이나 열에 놓인 돌멩이를 모두 줍는 방식.
운동장의 상태가 주어졌을 때, 최소 몇 번이나 달려가야 돌멩이 줍기를 끝낼 수 있는지 계산해라.

입력
n, k 제시. 500이하 10000이하
k개 줄 돌멩이 위치 한 줄에 하나 제시. 행 / 열 제시. 1이상인듯.

출력
첫 줄에 몇 번의 달리기를 통해 돌멩이를 전부 주울 수 있는지 출력

https://cocoon1787.tistory.com/819
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
            return True
    return False

n, k = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)

connect = [0]*(n+1)
ans = 0
for i in range(1, n+1):
    v = [0]*(n+1)
    if matching(i):
        ans += 1
print(ans)  

'''
def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if B[nx]==-1 or (not visited[B[nx]] and dfs(B[nx])):
            A[x]=nx
            B[nx]=x
            return 1
    return 0
input=__import__('sys').stdin.readline
n,k=map(int,input().split())
path=[[] for _ in range(n)]
for i in range(k):
    x,y=map(int,input().split())
    x-=1;y-=1
    path[x].append(y)
A=[-1]*n
B=[-1]*n
res=0
for i in range(n):
    if A[i]==-1:
        visited=[0]*n
        if dfs(i):res+=1
print(res)
'''
