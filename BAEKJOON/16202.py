'''
mst 게임

n개 정점, m개 양방향 간선 그래프.
임의의 두 정점 사이에 최대 1개의 간선이 있는 그래프이다.
mst 게임은 그래프에서 간선을 하나씩 제거하면서 mst의 비용을 구하는 게임이다.
k턴에 걸쳐 진행되며 첫 턴에는 입력으로 주어진 그래프의 mst 비용을 구해야 한다.
각 턴이 종료된 후 그 턴에서구한 mst에서 가장 가중치가 작은 간선 하나를 제거한다.
한 번 제거된 간선은 이후 턴에서 사용할 수 없다. 어떤 턴에서 mst 를 만들 수 없다면, 그 턴의 점수는 0이다. 이후 행동도 모두 0이다.
양방향 간선으로 이루어진 단순 그래프와 k가 주어졌을 때, 각 턴의 점수가 몇 점인지 구하는 프로그램을 작성하시오.

입력
정점 갯수 n, 간선 갯수 m, 턴 수 k 제시.
이후 m개 줄 간선의 정보 x,y 제시. 중복 간선 없음.
간선 가중치는 1,2,...n

출력 
한 줄에 공백 구분하여 k개 정수 출력. 각 턴에 얻는 점수
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1111)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y: return False
    if x > y:
        alive.remove(x)
        parent[x] = parent[y]
    else:
        alive.remove(y)
        parent[y] = parent[x]
    return True

n, m, k = map(int, input().rstrip().split())
egs, ans = [], []
for i in range(m):
    a, b = map(int, input().rstrip().split())
    egs.append((i+1, a, b))

for i in range(k):
    if m-i < n-1:
        ans.append(0)
        continue
    if ans and ans[-1] == 0:
        ans.append(0)
        continue
    hap = 0
    parent = [_ for _ in range(n+1)]
    alive = [_ for _ in range(1, n+1)]
    for j in range(i, m):
        v, a, b = egs[j]
        if union(a, b): hap+=v
    if len(alive) == 1:
        ans.append(hap)
    else:
        ans.append(0)

print(*ans)

'''
#1368번 : 물대기 - Gold 2
import sys
import heapq as hq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = 10**5 + 1
"""

"""
def find_parent(x):
    if parent[x] < 0 :
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return True
    if parent[px] > parent[py]:
        parent[py] += parent[px]
        parent[px] = py
    else:
        parent[px] += parent[py]
        parent[py] = px
    return False

def kruskal(n,n_list):
    total = 0
    count = 0
    for x,y,weight in n_list:
        if union(x,y):
            continue
        total += weight
        count += 1
        if count == n-1:
            return total
    return 0
n,m,k = map(int, input().split())
n_list = []
for i in range(m):
    a,b = map(int, input().split())
    n_list.append((a,b,i+1))

for i in range(k):
    parent = [-1] * (n + 1)
    print(kruskal(n,n_list), end=" ")
    del n_list[0]
'''



