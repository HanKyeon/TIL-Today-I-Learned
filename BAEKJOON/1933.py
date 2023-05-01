'''
스카이라인

n개 직사각형 모양 건물 제시. 스카이라인 구해라. 건물 전체의 윤곽.
각각 건물을 직사각형으로 표현했을 때, 그러한 직사각형들의 합집합.

입력
건물 갯수 n 제시.
n개 줄 n개 건물 정보. 왼쪽 x좌표, 높이, 우측 x좌표 제시.

출력
스카이라인 출력
출력 할 때는 높이가 변하는 지점에 대해서, 그 지점의 x좌표와 그 지점에서의 높이를 출력한다.
'''
import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
g = []
hl = [0] * n
q = []

end = [0] * n
v = set()
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    g.append((a, i, 1))
    g.append((c, i, 0))
    hl[i] = b
    end[i] = c
g.sort(key=lambda x : (x[0], -x[2], -hl[x[1]]))
maxh = 0
ans = []
for i in range(len(g)):
    x, idx, fla = g[i]
    if fla:
        if maxh < hl[idx]:
            maxh = hl[idx]
            ans.append((x, maxh))
        heappush(q, (-hl[idx], end[idx]))
    else:
        v.add(x)
        while q:
            if q[0][1] not in v:
                break
            heappop(q)
        if not q:
            if maxh:
                maxh = 0
                ans.append((x, maxh))
        else:
            if -q[0][0] != maxh:
                maxh = -q[0][0]
                ans.append((x, maxh))

for a, b in ans:
    print(a, b, end=' ')




###################################### 
import sys, heapq

# 입력부
n = int(sys.stdin.readline())
g = []
hl = [0] * n
q = []

# end : 현재 index번째 건물의 끝나는 지점을 저장하는 리스트
end = [0] * n
# v : 현재까지 끝난 끝점을 저장하는 set
v = set()
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    # 시작점이면 1, 끝점이면 -1
    g.append((a, i, 1))
    g.append((c, i, -1))
    hl[i] = b
    end[i] = c

# 그림 2, 그림3에 따라 정렬
# 첫번째 우선순위 : 시점이 앞서는지
# 두번째 우선순위 : 시점이 같다면 시작점인지
# 세번째 우선순위 : 시점도 같고 둘 다 시작점이면 높이가 더 높은지
g.sort(key=lambda x : (x[0], -x[2], -hl[x[1]]))

# maxh : 현재 최고높이
maxh = 0
ans = []
for i in range(len(g)):
    # x : 시점, idx : 건물의 인덱스, fla : 시작점인지 끝점인지
    x, idx, fla = g[i]
    
    # 시작점인 경우(빨간점)
    if fla == 1:
        # 높이가 갱신된다면 그 부분이 새로운 스카이라인
        if maxh < hl[idx]:
            maxh = hl[idx]
            ans.append((x, maxh))
        # 높이가 갱신됨과 상관없이 현재 건물의 높이와 끝점을 최대 힙에 저장
        heappush(q, (-hl[idx], end[idx]))
        
    # 끝점인 경우(파란점)
    else:
        # 현재 시점이 끝났기 때문에 set에 끝점의 시점을 저장
        v.add(x)
        # 최대 높이가 끝난 건물이 아닐때까지 pop
        while q:
            if q[0][1] not in v:
                break
            heappop(q)
            
        # 힙이 비었다면 스카이라인의 높이는 0으로 갱신
        if not q:
            if maxh:
                maxh = 0
                ans.append((x, maxh))
                
        # 힙이 있다면 현재 높이와 비교 시 변동이 있다면 그 높이가 그 다음으로 높은 건물이기 때문에
        # 스카이라인 높이 갱신
        else:
            if -q[0][0] != maxh:
                maxh = -q[0][0]
                ans.append((x, maxh))

# 정답 출력
for i in ans:
    print(i[0], i[1], end=' ')













