'''
중량제한

2이상 1만이하 n개의 섬으로 이루어진 나라. 섬 몇개 사이에는 다리가 있다.
두개의 섬에 공장을 세워 물품을 생산. 각 다리마다 중량 제한이 있다.
한 번의 이동에서 옮길 수 있는 물품들의 중량 최댓값을 구하는 프로그램 작성.

입력
n, m 제시. m은 1이상 10만이하. m개 줄에 정보 제시.
a, b, c 제시. 1이상n이하 a,b c는 1이상 10억이하
a번 섬과 b번 섬 사이 중량 제한이 C인 다리가 존재한다는 의미.
서로 같은 두 섬 사이에 여러개의 다리가 있을 수 있으며, 모든 다리는 양방향.
마지막 줄에는 공장이 위치해있는 두 섬의 번호 제시. 항상 이동 가능하다.

출력
답 출력
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x): # find parent 함수. 
    if parent[x] != x: # 자기 자신을 가르키고 있지 않다면
        parent[x] = find(parent[x]) # 가르키고 있는 값으로 부모를 찾으러 떠난다. 돌아오면 갱신.
    return parent[x] # 자기 자신이라면 값 반환, 자기 자신이 아니라면 위에서 갱신한 부모 값 반환.

def union(a, b):
    a = find(a) # a의 부모 노드
    b = find(b) # b의 부모 노드
    # 중간에 둘이 같다면 바로 끝내도 될듯?
    if a < b: # 더 작은 값을 부모로 설정해준다.
        parent[b] = a
        count[a] = max(count[a], count[b])
    else:
        parent[a] = b
        count[b] = max(count[b], count[a])


def check(a, b): # 같은 부모를 가졌는지 확인하는 함수.
    return find(a) == find(b)


n, m = map(int, input().rstrip().split())
parent = list(range(n+1)) # 부모를 가르키는 빠레뜨
count = [-int(10e9)] * (n+1) # 최대 운반량이므로 최소한으로. heap을 사용하기 위해 음수값으로.

heap = [] # 힙.
for _ in range(m):
    a, b, c = map(int, input().rstrip().split()) # a b 양방향, 비용 c.
    heappush(heap, (-c, a, b)) # 힙에 최대비용이 큰 순서대로 넣는다. 최소힙만 지원하니 -를 붙여서.
sta, end = map(int, input().rstrip().split()) # 시작값 끝값

while heap: # 힙이 있는 동안
    c, a, b = heappop(heap) # 힙에서 크기, 양방향노드 pop
    # print(a, b)
    union(a, b) # 양 노드 결합.
    root = find(a) # 두 노드의 부모가 같으니 그냥 a로 호출
    count[root] = max(count[root], c) # 카운트 루트에 c값을 비교해서 넣어준다.
    if check(sta, end): # 탈출 조건. 둘이 같은 부모를 가르키고 있다면
        print(-count[find(sta)]) # 부모 노드의 최댓값(음수 상태)에 음수를 붙여 정답 출력
        break # 탈출. 사실 탈출만 시키고 출력은 밖에서 해도 된다.
# print(count)
# print(parent)












