'''
맥주 마시면서 걸어가기

송도 펜타포트 락 페스티벌. 맥주 마시면서 걸어갈 것.
출발은 상근이네, 맥주 한 박스 들고 출발.
맥주 한 박스에는 맥주 20개.
50미터에 한 병 씩. 50미터를 가려면 그 직전에 맥주 한 벼응ㄹ 마셔야 한다.

박스에 들어있는 맥주는 20병을 넘을 수 없다. 편의점 나선 직후에도 맥주 한 병을 마셔야 한다.
편의점, 상근이네집, 락페 좌표 제시. 행복하게 도착 할 수 있는지 구해라.

입력
테케T 제시.
편의점 갯수 n 제시.
n개 줄
상근이네 집 sa, sb
n개 줄 편의점 a, b
락페 좌표 ea, eb
x,y 좌표가 있고, 좌표 간 거리는 맨해튼 거리이다.

출력
도착 가능하면 happy, 중간에 맥주가 바닥나면 sad 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

def check(h1, w1, h2, w2):
    return abs(h1-h2) + abs(w1-w2)

# 최대 1000m 이내만 이동 가능.
def bfs():
    global n, sh, sw, eh, ew
    if check(sh, sw, eh, ew) <= 1000:
        return "happy"
    q = deque([(sh, sw)])
    while q:
        h, w = q.popleft()
        for nh, nw in cvs:
            if cvs[(nh, nw)]:
                continue
            if check(h, w, nh, nw) > 1000:
                continue
            if check(nh, nw, eh, ew) <= 1000:
                return "happy"
            cvs[(nh, nw)] = 1
            q.append((nh, nw))
    return "sad"

for tc in range(int(input())):
    n = int(input())
    sh, sw = map(int, input().rstrip().split())
    cvs = {}
    for _ in range(n):
        a, b = map(int, input().rstrip().split())
        cvs[(a, b)] = 0
    eh, ew = map(int, input().rstrip().split())
    print(bfs())








