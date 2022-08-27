'''
마인크래프트

땅고르기 작업인데 이제 시간이 달라서 하나하나 확인하는게 나을듯한.

1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

1번 작업 2초 2번 작업 1초.
땅 고르기 작업에 걸리는 최소시간과 그 경우 땅의 높이
시작 할 때 가방에 B개의 블록이 존재. 땅의 높이는 256 블록을 초과 할 수 없으며 음수가 될 수 없다.

입력
N M B 제시. 1이상500이하 MN B는 0이상 64000000 6400만 이하
N개 줄에 M개의 정수로 땅의 높이 제시.
'''
# 파이파이 통과

def wim(num):
    global n, m, s
    if n*m*num <= s:
        return True
    else:
        return False

n, m, b = map(int, input().split())
g = []
for _ in range(n):
    a = list(map(int, input().split()))
    g.extend(a)
s = sum(g)+b # 기용 가능한 블록 갯수
av = s // (n*m) + 1
hei = []
for i in range(min(g), max(g)+1):
    if wim(i): # 이 높이를 만들 수 있는가?
        ti = 0
        for j in g: # 이 작업 중 백트래킹이 가능하다!
            if j - i > 0:
                ti += (j-i)*2
            elif j - i < 0:
                ti += (i-j)
        hei.append((ti, i))
a = sorted(hei, key=lambda x:(x[0],-x[1]))
print(a[0][0], a[0][1])

# 파는데 2초
# 꺼내는데 1초
'''
따라서 sum ng가 n*m
가방에 10 -> 10초
20 20 20 20 20 10
'''
'''
# 파이썬 통과
N, M, B = map(int,input().split())
import sys
ground = []
from collections import Counter
for i in range(N):
    ground += map(int,sys.stdin.readline().split())
answer_height = 0
answer_time = 10000000000
_sum = sum(ground)
ground=Counter(ground)
for height in range(min(ground), max(ground)+1):
    if B + _sum >= height * N * M:
        time = 0
        for i in ground:
            if i < height:
                time += (height-i) * ground[i]
            elif i >= height:
                time +=2*(i-height) * ground[i]
        if time <= answer_time:
            answer_height = height
            answer_time = time

print(answer_time, answer_height)
'''

