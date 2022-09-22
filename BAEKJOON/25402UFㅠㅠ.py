'''
트리와 쿼리

1부터 n까지 n개 정점으로 이뤄진 트리. i번째 간선은 서로 다른 두 정점 ai bi. 잇는다.
n개의 정점 중 몇 개를 골라 그 고른 정점들을 s{s1...sk} 라고 하자. 또한 si=v를 만족하는 i가 존재 할 때, 정점 b가 s에 속한다고 부르자. s에 속하는 서로 다른 두 정점 u, v에 대해 s에 속하는 정점만을 이용해 트리 위에서 u, v 사이를 오갈 수 있다면 u와 v는 s 위에서 연결되어 있다고 하자.

다음 조건을 만족하는 정점 쌍의 갯수를 s의 연결 강도.
u와 v는 서로 다른 정점.
u<v 존재하는 정점
S 위에서 연결되어 있다.
고른 정점들 S가 주어질 때, S의 연결 강도를 계산하는 프로그램을 작성하라. 질의 Q개에 대해 모두 답해야 한다.

입력
정수 N
간선 정보 제시. i번째 줄에는 두 정수 Ai, Bi 제시.
다음 줄 정수 Q
Q개의 질의 정보 제시.
i번째 질의를 나타내며, 정수 k와 k개의 정수 차례 제시.

출력
Q개 줄에 걸쳐 질의에 대한 답 출력. i번째 줄에는, i번째 질의에서 주어진 S에 대하여 S의 연결 강도를 출력한다.

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(260000)

def dfs(num):
    global nsum
    for i in g[num]:
        if i in setkl:
            nsum += 1
            setkl.remove(i)
            dfs(i)

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    g[b].append(a)
    g[a].append(b)

q = int(input())
for _ in range(q):
    kl = list(map(int, input().rstrip().split()))
    k = kl.pop(0)
    setkl = set(kl)
    # print('setkl : ',setkl)
    ans = 0
    for i in kl:
        if i not in setkl:
            continue
        nsum = 1
        setkl.remove(i)
        dfs(i)
        ans += (nsum**2-nsum)//2
    print(ans)




'''
7
1 2
1 3
1 5
2 7
4 6
4 7
6
1 1
2 1 2
4 1 2 3 4
5 1 2 4 6 7
6 1 2 3 4 5 6
7 1 2 3 4 5 6 7
'''







'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
parent = [i for i in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    a, b = find(a), find(b)
    if a == b:
        continue
    union(a, b)
q = int(input())
for _ in range(q):
    cnt = {}
    kl = list(map(int, input().rstrip().split()))
    k = kl.pop(0)
    for i in range(k):
        root = find(kl[i])
        if cnt.get(root, 0):
            cnt[root] += 1
        else:
            cnt[root] = 1
    print(cnt)
'''










