'''
숨바꼭질 5

수빈이는 현재 n, 동생은 k. 걷거나 순간이동.
x일 때 걸으면 1초 후 x-1 or x+1. 순간이동은 1초 후 2*x.
동생은 걷기만 한다. 이동은 가속이 붙는다. 이전에 이동한 거리보다 1을 더한 만큼 이동.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하시오.
동생을 찾는 위치는 정수 좌표, 수빈이가 0보다 작은 좌표로, 50만보다 큰 좌표로 이동하는 것은 불가능.

입력
1줄에 수빈이가 있는 위치 n과 동생이 있는 위치 k가 주어진다. n과 k는 정수.

출력
수빈이가 동생을 찾는 가장 빠른 시간 출력. 찾을 수 없거나 위치가 50만을 넘는 경우 -1 출력.
'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
if n==k:
    print(0)
    exit()

v = [[0,0] for _ in range(500001)]
q = deque([(n, False)])
while q:
    num, flag = q.popleft()
    for i in [num*2, num+1, num-1]:
        if 0<=i<=500000 and not v[i][not flag]:
            v[i][not flag] = v[num][flag]+1
            q.append((i, not flag))
v[n][0] = 0

q = deque([(k, 0)])
ans = 1000
while q:
    num, cnt = q.popleft()
    if cnt >= v[num][cnt%2]:
        if ans > cnt:
            ans = cnt
    if num+cnt < 500000:
        q.append((num+cnt+1, cnt+1))
ans = -1 if ans == 1000 else ans
print(ans)


'''
7 37
5

10 57
5

21 70
4

18 58
4

18 66
4

16 50
4

34 0
8
'''