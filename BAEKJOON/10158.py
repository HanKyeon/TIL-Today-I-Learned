'''
개미

가로w 세로h 격자
p, q에 개미. 우상단 45도로 출발 1시간 뒤 p+1, q+1
경계면에 부딪치면 같은 속력으로 반사되어 이동
개미의 t시간 후 위치는?

입력
w h 2이상 4만 이하
p q 0~w 0~h
t 1이상 2억이하

출력
t시간 후 개미 좌표 x, y
'''
# 입력
w, h = map(int, input().split())
x, y = map(int ,input().split())
t = int(input())
x, y = (x + t) % (2 * w), (y + t) % (2 * h)
if x >= w : x = w - x % w
if y >= h : y = h - y % h
# 출력
print(x, y)

