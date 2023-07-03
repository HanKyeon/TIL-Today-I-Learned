'''
사자와 토끼

2플레이어 1심판
n개 수풀 m개 오솔길. 오솔길은 양방향 연결

1. 심판이 사자와 토끼의 초기 위치를 각각 어느 수풀로 할 지 정한다. 같을 수 없으며 사자의 위치는 사자한테만, 토끼는 토끼에게만 알려준다.
2. 매 턴마다 사자와 토끼는 현재 위치한 수풀에서 오솔길 1개를 따라 이동한다.
3. 이동한 뒤 같은 위치라면 사자가 토끼를 먹고 끝. 아니라면 반복. 같은 오솔길을 통해 이동해도 서로 다른 수풀에 도달했다면 안끝난다.

근데 영원히 안끝나는 초기 위치 조합이 있다. 영원히 안끝나는 초기 위치 경우의 수 갯수 구하시오.

입력
n, m 제시
m개 줄 a, b 제시. a와 b 연결.

출력
끝나지 않는 초기 위치 경우의 수 출력
'''
'''
이분 그래프일 경우에 결론이 나지 않는다. (1707 참고)
이분 그래프를 참 / 거짓으로보면 참 거짓에 토끼 사자 있는 경우가 있으므로 참갯수*거짓갯수*2가 답
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(idx):
    global n
    v[idx] = 1
    q = deque([(idx, 1)])
    while q:
        num, fla = q.popleft()
        for i in g[num]:
            nfla = 0 if fla else 1
            if v[i] < 0:
                v[i] = nfla
                q.append((i, nfla))
            elif v[i] != nfla:
                return False
    return True

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)
v = [-1]*(n+1)
for i in range(1, n+1):
    if v[i] < 0:
        ans = bfs(i)
        if not ans: break
if not ans:
    print(0)
    exit()
v.pop(0)
cnt1 = v.count(1)
cnt2 = n-cnt1
print(cnt1*cnt2*2)
