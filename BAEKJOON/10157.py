'''
자리 배정

가로C 세로R 격자형 좌석 배치. x, y로 표기. 
좌하단 1,1 우상단 C, R
시계 방향으로 회전 회오리
대기순번 K인 사람의 좌표x, y 찾기

입력
c, r 5이상 1000이하
대기번호 k

출력
k번째 관객의 좌석번호 x y. 숫자 넘어가면 0 출력.
k는 1이상 1억 이하
c, r은 5 이상 1000 이하.

주의점
# R*C로 만들어서 인덱싱 한다!
# =좌하단이 기준인 수학적인 방식으로 본다.
# 0 인덱스 없다!
# 1,1부터 중앙으로 회전 회오리!
# 찾는 것이 메인이다.
'''
# 입력
c, r = map(int,input().split())
k = int(input())
# 범위 벗어나면 0 출력
if k > c * r :
    print(0)
else :
    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    # 그래프
    g = [[0] * c for _ in range(r)]
    x, y = 0, 0 # 시작점
    d, ct = 0, 0 # 방향, 시작 숫자
    while ct <= c * r :
        ct += 1
        if ct == k : # 목표 번호면
            print(y+1,x+1)
            break
        g[x][y] = ct # 방문처리
        nx, ny = x + dx[d], y + dy[d] # 새 좌표
        if 0 <= nx < r and 0 <= ny < c and g[nx][ny] == 0 : # 좌표내이고, 0이라면
            x, y = nx, ny # 바꿔서 진행
        else : # 아니면 방향 바꿔서 한 번 진행
            d = (d + 1) % 4
            x += dx[d]
            y += dy[d]
















'''
# 입력
w, h = map(int, input().split())
k = int(input())
if k > w*h:
    print(0)
elif w==1 or h == 1 :
    if w==1:
        print(f"1 {k}")
    elif h==1:
        print(f"{k} 1")
else : # 아니라면 이 아래 실행
    m = min(w//2, h//2) # 얼마나 회전하는지
    ns = [1] * m # 좌하단 숫자 리스트
    hn = 0 # 첫바퀴 이후 회전 반복 횟수
    if m > 0: # 회전을 첫바퀴 이후로 몇번 더 한다면
        cw, ch = w, h # 그 때의 좌하단 값 저장
        for i in range(1, m):
            ns[i] = ns[i-1] + (cw-1+ch-1)*2
            cw, ch = cw-2, ch-2
    for i in range(m): # 회전 몇번 한 뒤에 나오는지 체크
        if k >= ns[i] :
            hn = i
    nw, nh = w-hn*2, h-hn*2
    ki = ns[hn]
    chai = k - ki
    print(nw, nh, chai, hn)
    # 출력
    if 0 <= chai <= nh-1:
        print(f"{0+1+hn} {chai+1+hn}")
    elif nh-1 <= chai <= nh+nw-2:
        print(f"{chai-(nh-1)+1+hn} {nh-1+1+hn}")
    elif nh+nw-2 <= chai <= 2*nh+nw-3:
        print(f"{nw-1+1+hn} {nh-1-(chai-nh+nw-2)+1+hn}")
    else :
        print(f"{nw-1-(chai-(2*nh+nw-3))+1+hn} {0+1+hn}")


'''
# 38%

'''
w 7 h 6
높이가 1이면 그대로
2이면 꼭지점의 사잇값을 찾는 방식.
가로 // 몫 혹은 세로 // 목
h = 6 w = 7
0, 0 = 1+h-1
1, 1 = 1+h-1 + w-1 h-1 w-2 h-2 / 6 6 5 5 4
2, 2 = 

1 6 12 17 = 1 / h / h+w-1 / h+w-1+h-1
23 26 30 33 1+(w-1+h-1)*2 / 점1 + h-2 / 점2 + 
36 38 40 41
'''
# 1. 그래프 만들기
# 2. 숫자 찾기 함수로 하여 return을 0 혹은 좌표로 만들자.








