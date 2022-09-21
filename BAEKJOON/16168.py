'''
퍼레이드

종우는 18학번을 대표하여 중앙대학교 개교 100주년 기념 퍼레이드의 경로 선정 위원으로 선정되었다. 퍼레이드의 경로는 일정한 지점들과 두 지점을 연결하는 연결 구간으로 이루어져 있다. 종우는 모든 지점을 지나면서 모든 연결 구간들을 지나고 싶어한다.

하지만 같은 연결 구간을 두 번 이상 지날 경우 그 구간의 주민들이 민원을 제기하게 된다. 단, 같은 지점은 두 번 이상 지나도 된다.

민원을 받지 않으면서 모든 구간을 지나도록 퍼레이드를 만들고 싶은 종우를 위한 프로그램을 작성해보도록 하자.

입력
노드 갯수v, 연결 갯수 e
연결구강늬 두 지점 v1, v2 제시. 중복세히 없고 적어도 하나의 연결 보장.

출력
가능하면 YES 불가능하면 NO0
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find해서
    if x<y:
        parent[y] = x
    else:
        parent[x] = y

v, e = map(int, input().rstrip().split())
parent = list(range(v+1))
# g = [[] for _ in range(v+1)]
g = [0]*(v+1)
for _ in range(e):
    a, b = map(int, input().rstrip().split())
    g[a] += 1
    g[b] += 1
    # g[a].append(b)
    # g[b].append(a)
    a, b = find(a), find(b)
    union(a, b)
ans = ''
for i in range(2, v+1):
    if find(i) != 1:
        ans = 'NO'
        break
if not ans:
    cnt = 0
    for i in g:
        if i % 2:
            cnt += 1
    if cnt == 0 or cnt == 2:
        ans = 'YES'
    else:
        ans = 'NO'
print(ans)















