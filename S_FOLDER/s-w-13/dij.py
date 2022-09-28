'''
다익스트ㅏㄹ ㄱㄱ
0번노드에서 n-1까지 최단 경로 출력
'''

from heapq import heappop, heappush

for tc in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        g[a].append((c, b))
    heap = [(0, 0)]
    dst = [int(10e9)]*n
    vst = [0]*(n)
    dst[0] = 0
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        vst[nod] = 1
        for co, nnod in g[nod]:
            if vst[nnod]:
                continue
            if cost+co < dst[nnod]:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    print(f"#{tc} {dst[-1]}")


