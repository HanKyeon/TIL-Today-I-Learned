'''
네크워크 복구

1이상 1000이하 컴퓨터로 구성 된 네트워크. 연결되어 있어 두 컴퓨터 간 통신 가능. 통신을 할 때 서로 직접 연결되어 있는 회선을 이용 할 수 있으며, 다른 컴을 거쳐 통신 가능하다.
간선에 가중치가 있다.
해커 칩입, 네트워크를 복구 할 것이다.
하나 공격 받으면 슈퍼컴이 간선으로 전달 받고, 슈퍼컴이 간선으로 보안 패킷 전송 하는 방식.
1. 해커가 다시 공격 할 수 있기 때문에, 최소 갯수의 회선만 복구 할 것이다. 네트워크를 복구 한 후, 서로 다른 두 컴퓨터 간에 통신이 가능하도록 복구해야한다.
2. 네트워크를 복구해서 통신하게 하는 것도 중요하지만, 해커에게 공격을 받았을 때 보안 패킷을 전송하는데 걸리는 시간도 중요한 문제가 된다. 따라서 슈퍼컴과 다른 컴을 통신하는데 걸리는 시간이 원래 네트워크에서 통신하는데 걸리는 최소 시간보다 커지면 안된다.

원래의 네트워크가 주어졌을 때, 조건을 만족하며 네트워크를 복구하는 방법을 알아내는 프로그램 작성.

입력
n, m 제시. m개 줄에 회선 정보 a, b, c 제시. A와 B 간 통신 시간이 c인 회선으로 연결되어 있다. 컴은 1번부터 n까지의 정수이며, 1번컴은 슈퍼컴 루트이다. 모든 통신은 완전 쌍방향.

출력
첫째 줄에 복구 할 회선의 갯수 k개를 출력한다.
다음 k개의 줄에는 복구한 회선을 나타내는 두 정수 a, b를 출력.
a번 컴과 b번 컴을 연결하던 회선을 복구한다는 의미. 출력은 임의의 순서대로 하며 답이 여러 개 존재하는 경우에는 아무거나 하나 출력해라.
루트에서의 최단 경로만 찾아내기?
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij(sta):
    global m, n
    dst = [0]+[int(10e9)]*n
    dst[sta] = 0
    heap = [(0, sta, 0)]
    ret = set()
    while heap:
        cost, nod, frm = heappop(heap)
        if dst[nod] < cost:
            ret.remove((min(nod, frm), max(nod, frm)))
            continue
        for co, nnod in g[nod]:
            if dst[nnod] > cost+co:
                dst[nnod] = cost+co
                ret.add((min(nod, nnod), max(nod, nnod)))
                heappush(heap, (cost+co, nnod, nod))
    return ret

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
ans = dij(1)
print(len(ans))
for i in ans:
    print(*i)

















