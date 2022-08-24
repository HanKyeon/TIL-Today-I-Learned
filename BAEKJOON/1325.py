'''
효율적인 해킹

N개의 컴퓨터.
신뢰와 비신뢰 관계로 이루어져 있다.
A가 B를 신뢰하는 경우, B를 해킹하면 A도 해킹 가능.
신뢰 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹 할 수 있는 번호를 출력하시오.

입력
N과 M 제시. n은 만이하 자연수 M은 10만이하 자연수
M개 줄에 신뢰관계 제시. A가 B를 신뢰한다.
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(num):
    global n, ans
    v = [0] * (n+1)
    q = deque()
    q.append(num)
    v[num] = 1
    while q:
        nn = q.popleft()
        for i in g[nn]:
            if v[i] == 0:
                v[i] = 1
                q.append(i)
    return sum(v)

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    g[b].append(a)
ans = [0] * (n+1)
for i in range(1, n+1):
    ans[i] = bfs(i)
a = [i for i, v in enumerate(ans) if v == max(ans)]
if a[0] == 0: a.remove(0)
print(*a)


'''
import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10000000)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
scc=[-1]*(n+1)
scc_num=0
d=[0]*(n+1)
finished=[False]*(n+1)
node_idx=0
st=[]
scc_size=[]
def dfs(x):
    global node_idx,scc_num
    node_idx+=1
    d[x]=node_idx
    st.append(x)
    parent=d[x]
    for y in graph[x]:
        if d[y]==0:
            parent=min(parent,dfs(y))
        elif not finished[y]:
            parent=min(parent,d[y])
    if parent==d[x]:
        scc_size_num=0
        while True:
            scc_size_num+=1
            s=st.pop()
            scc[s]=scc_num
            finished[s]=True
            if s==x:
                break
        scc_num+=1
        scc_size.append(scc_size_num)
        
    return parent

    
for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)

for j in range(1,n+1):
    if d[j]==0:
        dfs(j)

scc_graph=[set() for _ in range(scc_num)]
scc_graph_inv=[set() for _ in range(scc_num)]

for i in range(1,n+1):
    for j in graph[i]:
        if scc[i]!=scc[j]:
            scc_graph[scc[i]].add(scc[j])
            scc_graph_inv[scc[j]].add(scc[i])

scc_graph_outnum=[len(scc_graph[i]) for i in range(scc_num)]

scc_childs=[set() for _ in range(scc_num)]
q=[i for i in range(scc_num) if scc_graph_outnum[i]==0]
while q:
    temp=[]
    for i in q:
        scc_childs[i].add(i)
        for j in scc_graph_inv[i]:
            scc_childs[j]|=scc_childs[i]
            scc_graph_outnum[j]-=1
            if scc_graph_outnum[j]==0:
                temp.append(j)
    q=temp
node_child_num=[sum(scc_size[j] for j in scc_childs[i]) for i in range(scc_num)]
m=max(node_child_num)

for i in range(1,n+1):
    if node_child_num[scc[i]]==m:
        print(i,end=" ")
'''


