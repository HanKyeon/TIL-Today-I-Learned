# 테스트 케이스 t
for t in range(int(input())) :
    c = 0 # 카운트
    x1, y1, x2, y2 = map(int, input().split())
    # 1과 2의 거리 : ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    n = int(input()) # 행성 갯수
    for _ in range(n) : #만큼 반복
        cx, cy, r = map(int, input().split()) 
        # 행성계가 곂치거나, 닿거나 하지 않으므로 두개 다 안에 있거나 밖에 있을 때는
        # 카운트를 올리지 않음
        if ((x1-cx)**2 + (y1-cy)**2)**(1/2) < r and ((cx-x2)**2 + (cy-y2)**2)**(1/2) < r :
            continue
        elif ((x1-cx)**2 + (y1-cy)**2)**(1/2) > r and ((cx-x2)**2 + (cy-y2)**2)**(1/2) > r :
            continue
        else :
            c+=1
    
    print(c)
    