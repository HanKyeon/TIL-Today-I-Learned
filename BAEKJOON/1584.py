'''
게임

들어갈 수 없는 죽음의 구역, 들어가서 한 번 움직일 때마다 생명 1씩 소모되는 위험 구역 존재. 자유롭게 움직이는 안전 구역.
0,0에서 500,500으로 가야한다. 상하좌우 이동. 잃는 생명의 최솟값을 구해라.

입력
위험 구역 수 n 제시.
n개 줄 x1,y1,x2,y2로 위험구역 제시.
죽음 구역 수 m 제시.
m개 줄 죽음 구역 x1,y1,x2,y2 제시
위험 구역이 아무리 겹쳐도 생명은 1씩 감소. 시작 지점은 생명 감소x 죽음 구역 역시 x

출력
소모되는 생명 최솟값 출력. 갈 수 없다면 -1
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def fill(x1, y1, x2, y2, v):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            g[i][j] = v

def lego():
    heap = [(0, 0, 0)] # 생명 h w
    v = [[3333]*501 for _ in range(501)]
    v[0][0] = 0
    while heap:
        life, h, w = heappop(heap)
        if h==500 and w==500:
            return life
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<=500 and 0<=nw<=500 and not g[nh][nw] < 0:
                if not g[nh][nw] and v[nh][nw] > life:
                    v[nh][nw] = life
                    heappush(heap, (life, nh, nw))
                elif g[nh][nw] and v[nh][nw] > life+1:
                    v[nh][nw] = life+1
                    heappush(heap, (life+1, nh, nw))
    return -1

mov = [(-1,0),(0,1),(1,0),(0,-1)]
g = [[0]*501 for _ in range(501)]
for i in range(int(input())):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    fill(x1,y1,x2,y2,False)
for i in range(int(input())):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    fill(x1,y1,x2,y2,True)
print(lego())


'''
# 빠른 코드
from collections import deque
import sys
input = sys.stdin.readline


def making(num):
    x1, y1, x2, y2 = ipt
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y2, y1 = y1, y2
    
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            area[i][j] = num
            

def zero_one_bfs():
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    q = deque()
    q.append((0, 0, 0))
    
    visited = [[False]*501 for _ in range(501)]
    visited[0][0] = True
    
    while q:
        x, y, lost = q.popleft()
        if x==500 and y==500:
            return lost
        
        for a, b in go:
            pp, qq = x+a, y+b
            if pp < 0 or pp > 500 or qq < 0 or qq > 500:
                continue
            if visited[pp][qq]:
                continue
            if area[pp][qq] == 2:
                continue
            
            visited[pp][qq] = True
            if not area[pp][qq]:
                q.appendleft((pp, qq, lost))
            else:
                q.append((pp, qq, lost+1))
    
    return -1       
        
            
area = [[0]*501 for _ in range(501)]
for n in range(2):
    for _ in range(int(input())):
        ipt = list(map(int, input().split()))
        making(n+1)

print(zero_one_bfs())
'''
