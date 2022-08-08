'''
직사각형

입력
4개의 줄. 8개의 정수 x1,y1,x2,y2 순.
첫 4개는 첫번째 직사각형, 나머지4는 두번째 직사각형
좌표는 1이상 5만이하의 정수로 제한.

출력
공통 부분이 직사각형a 선분b 점c 없음d로 출력
'''
def rectangle(box1, box2) :
    



for _ in range(4) :
    nl = list(map(int, input().split()))
    b1, b2 = nl[:4], nl[4:]






'''
안에 들어갈 때
x1<x3<x4<x2
y1<y3<y4<y2

x3<x1<x2<x4
y3<y1<y2<y4

곂칠 때
x1 x3 x2 x4
y1 y3 y2 y4

x3 x1 x4 x2
y3 y1 y4 y2

십자 모양 곂칠 때
x1 x3 x4 x2
y1 y3 y4 y2

x3 x1 x2 x4
y3 y1 y2 y4

직선일 때
r1의 작은 x혹은 y와 r2의 큰x 혹은 y와 같다. 나머지는 다르다.

큰 값이 작은값보다 크다.
'''