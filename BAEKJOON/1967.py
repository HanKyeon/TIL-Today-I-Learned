'''
트리의 지름

트리 간선에 가중치 존재.
두 노드 사이의 거리가 가장 긴 것은 트리의 지름이다. 트리의 지름을 구해라.

입력
노드 수 n
간선 정보. 3개 정수.
부모노드, 자식노드, 간선 가중치.
간선 정보는 부모 노드의 번호가 작은 것 먼저 입력. 부모 노드의 번호가 같으면 자식 번호가 작은 것이 먼저 제시.
루트 노드는 항상 1 가중치는 100이하 양정수.

출력
트리 지름 출력
'''

# 스스로 연 헬게이트. 2진트리+dp로 시작했다가 조건 덕지덕지 달려서 pypy로만 돌아간다.
# 위상정렬+dp를 엮은 풀이이다.
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]
reqn = [0]*(n+1)
dp = [[0, 0] for _ in range(n+1)]
prtc = [[] for _ in range(n+1)]
for _ in range(n-1):
    prt, cld, cst = map(int, input().rstrip().split())
    reqn[prt]+=1
    g[cld] = [prt, cst]
li = [i for i, v in enumerate(reqn) if v == 0]
li.pop(0)
if n==1:
    li.pop()
q = deque(li)
while q:
    cld = q.popleft()
    prt, cst = g[cld]
    dp[prt][1] = max(dp[prt][1], dp[cld][1]+cst)
    prtc[prt].append(dp[cld][1]+cst)
    dp[prt][0] = max(dp[prt][0], dp[cld][1]+cst)
    reqn[prt] -= 1
    if reqn[prt] == 0:
        for i in range(len(prtc[prt])):
            for j in range(i+1, len(prtc[prt])):
                dp[prt][0] = max(prtc[prt][i]+prtc[prt][j], dp[prt][0])
        if prt != 1:
            q.append(prt)
if n == 1:
    ans = 0
else:
    ans = max(list(zip(*dp))[0])

print(ans)



'''
# 빠른 코드
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def 함수(root, dep):
    global ans
    ml = 0
    ml2 = 0
    for i, j in g[root]:
        l = 함수(i, dep)+j
        if l > ml:
            ml2 = ml
            ml = l
        elif l > ml2:
            ml2 = l
            
    r = ml+max(ml2, dep)
    ans = max(ans, r)
    return ml

n = int(input())
g = [[] for _ in range(n+1)]
ans = 0
for _ in range(n-1):
    prt, cld, cst = map(int, input().rstrip().split())
    g[prt].append((cld, cst))
함수(1, 0)
print(ans)
'''



















