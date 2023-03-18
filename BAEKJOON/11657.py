'''
타임머신

n개의 도시. 버스 m개.
a 시작 도시 b 도착 도시 c 버스 타고 이동하는 시간. c는 양수가 아닐 수 있음. 시간을 되돌아가는 경우임.
1번에서 출발해 나머지 도시로 가는 가장 빠른 시간을 구해라.

입력
도시 n, 노선 갯수 m 제시.
m개 줄 a, b, c 제시.

출력
사이클 존재 시 -1. 아니라면 n-1개 줄에 1부터 n까지 가장 빠른 시간 출력
경로가 없어도 -1 출력.
'''
import sys
input = sys.stdin.readline

def bf():
    for i in range(1, n+1):
        for co, nod, nnod in g:
            if dst[nod] != int(10e9) and dst[nnod] > dst[nod]+co:
                dst[nnod] = dst[nod]+co
                if i == n:
                    return True
    return False

n, m = map(int, input().rstrip().split())
g = []
for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    g.append((c, a, b))

dst = [int(10e9) for _ in range(n+1)]
dst[1] = 0
if bf():
    print(-1)
else:
    for i in range(2, n+1):
        print(dst[i]) if dst[i] != int(10e9) else print(-1)





