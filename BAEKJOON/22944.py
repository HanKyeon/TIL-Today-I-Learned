'''
죽음의 비

n*n 격자. 두곳 제외 체력 1씩 감소. 안전지대로 이동해야 함.
우산 K개 존재. 우산 내구도 D. 비 맞으면 내구도 1 감소, 내구도 0되면 사라짐. 내구도 통일

1. 상하좌우 이동
2. 안전하면 반복 종료
3. 우산 있다면 우산 든다. 기존 우산 버리고 바꾼다.
4. 가지고 있는 우산 내구도 1 감소, 없다면 체력 1 감소
5. 우산 내구도 0이면 우산 사라짐.
6. 체력 0되면 사라짐
7. 반복

입력
n, h, d 제시. 크기 체력 우산
n개 줄 격자 정보 제시. 우산 U 현재S 안전E 빈칸. 메인 그시기는 반드시 한 칸 씩 존재

출력
안전지대로 이동할 때 최소 이동 횟수 출력 못가면 -1
'''
import sys
from collections import deque
input = sys.stdin.readline

mov = [(-1, 0),(0, 1),(1, 0),(0,-1)]

def bfs():
    global n, eh, ew, d
    while q:
        h, w, hp, umb, cnt = q.popleft()
        if hp < 0:
            break
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n:
                if g[nh][nw] == ".":
                    if nh == eh and nw == ew:
                        return cnt+1
                    if umb and v[nh][nw] < hp:
                        v[nh][nw] = hp
                        q.append((nh, nw, hp, umb-1, cnt+1))
                    elif v[nh][nw] < hp-1:
                        v[nh][nw] = hp-1
                        q.append((nh, nw, hp-1, umb, cnt+1))
                else:
                    if v[nh][nw] < hp:
                        q.append((nh, nw, hp, d-1, cnt+1))
                        v[nh][nw] = hp
                    
    return -1

n, h, d = map(int, input().rstrip().split())
g = []
sh, sw, eh, ew = 0, 0, 0, 0
for i in range(n):
    s = list(input().rstrip())
    for j in range(n):
        if s[j] == "S":
            sh, sw = i, j
            s[j] = '.'
        elif s[j] == "E":
            eh, ew = i, j
            s[j] = '.'
    g.append(s)
v = [[0]*n for _ in range(n)]
v[sh][sw] = h
q = deque([(sh, sw, h, 0, 0)])
print(bfs())

'''
# 빠른 코드

"""
N, H, D의 크기를 볼 때 메모이제이션을 하기는 어렵다.
좌표평면에서 bfs를 할 때 중복 방문을 어떻게 배제해야 할 지 모르겠다.
그래프의 관점으로 접근하면 좀 나을 것이다.
노드의 개수는 총 K + 2 ( K <= 10 ) 이므로,
노드 간의 맨해튼 거리를 구하고 다익스트라를 사용하는데, S에서 출발할 때만 거리에 H를 상한선으로 두고,
U에서 출발할 때는 거리에 D를 상한선으로 두면 된다.
[1차 채점] WA.
S에서 출발해서 우산에 도착하고 남은 H를 다시 사용할 수 있다는 점을 간과했다.
[2차 채점] WA.
이미 방문한 지점을 방문할 수 있어야 한다.
단, 쓸데없는 이동으로 인한 무한 루프는 예방해줘야 한다.
[3차 채점] WA.
우산이 있는 지점에도 비는 내린다.
"""
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, h, d = map(int, input().split())
    grid = [input() for _ in range(n)]
    nodes = []
    for col in range(n):
        for row in range(n):
            if grid[col][row] != '.':
                nodes.append((col, row))
    dists = [[0 for row in range(len(nodes))] for col in range(len(nodes))]
    for a in range(len(nodes) - 1):
        for b in range(a + 1, len(nodes)):
            dist = abs(nodes[a][0] - nodes[b][0]) + abs(nodes[a][1] - nodes[b][1])
            dists[a][b] = dists[b][a] = dist
    for idx, (col, row) in enumerate(nodes):
        if grid[col][row] == 'S':
            start = idx
        elif grid[col][row] == 'E':
            end = idx
    heap = [(dist, h - dist + 1, node, (1 << start) | (1 << node)) for node, dist in enumerate(dists[start])\
            if dist <= h and node != start]
    heapq.heapify(heap)
    while heap:
        curr_dist, curr_health, curr_node, bit_visit = heapq.heappop(heap)
        if curr_node == end:
            print(curr_dist)
            return
        for next_node, dist in enumerate(dists[curr_node]):
            if bit_visit & (1 << next_node) == 0:
                if dist <= d:
                    heapq.heappush(heap, (curr_dist + dist, curr_health, next_node, bit_visit | (1 << next_node)))
                elif dist - d < curr_health:
                    heapq.heappush(heap, (curr_dist + dist, curr_health - (dist - d), next_node, bit_visit | (1 << next_node)))
    print(-1)


if __name__ == '__main__':
    main()

'''
