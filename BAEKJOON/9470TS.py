'''
Strahler 순서

지질학에서 하천계는 유향 그래프로 나타낼 수 있다.
강은 간선, 물의 방향은 간선의 방향. 노드는 호수나 샘처럼 강이 시작하는 곳, 강이 합쳐지거나 나눠지는 곳, 바다와 만나는 곳

강의 근원인 노드 순서는 1
나머지 노드는 그 노드로 들어오는 강의 순서 중 가장 큰 값을 i라고 했을 때 들어오는 모든 강 중에서 Strahler 순서가 i인 강이 1개면 순서는 i, 2개 이상이면 순서는 i+1이다.
하천계 정보다 주어졌을 때 스트라흘러 순서를 구해라.

입력
테케T 제시.
k m p 제시. 테케 번호, 노드 수, 간선 수
p개 줄 간선 정보 제시. a, b. a에서 b로 흐른다.
m은 항상 바다와 만나는 노드, 밖으로 가는 간선 x

출력
테케마다 테케 번호와 입력으로 주어진 하천계의 스트라흘러 순서를 한 줄에 하나씩 출력.
'''
from collections import deque
import sys
input = sys.stdin.readline

for tc in range(1, int(input())+1):
    _, n, m = map(int, input().rstrip().split())
    reqn = [0]*(n+1)
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        reqn[b] += 1
        g[a].append(b)
    sth = [[] for _ in range(n+1)]
    nbr = [0]*(n+1)
    q = deque()
    for i in range(1, n+1):
        if reqn[i] == 0:
            nbr[i] = 1
            q.append(i)
    while q:
        num = q.popleft()
        for i in g[num]:
            reqn[i] -= 1
            sth[i].append(nbr[num])
            if reqn[i] == 0:
                q.append(i)
                a = max(sth[i])
                if sth[i].count(a) == 1:
                    nbr[i] = a
                else:
                    nbr[i] = a+1
    print(tc, max(nbr))










