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
    x1, y1, x2, y2 = box1
    x3, y3, x4, y4 = box2
    # 박스의 왼쪽 좌표가 오른쪽 좌표보다 크면 안곂친다.
    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        return("d")
    # x가 하나 곂치면
    if x2==x3 or x4==x1:
        # 점
        if y2==y3 or y4==y1:
            return ("c")
        # y가 만나지 않는 경우는 위에서 처리됨
        else:
            return("b")
    # 점인 경우 처리되었고 안곂치면 d 반환해둠.
    if y2==y3 or y4==y1:
        return("b")
    # 나머진 네모네모
    return("a")
# 입 실 출
for _ in range(4) :
    nl = list(map(int, input().split()))
    b1, b2 = nl[:4], nl[4:]
    print(rectangle(b1, b2))




