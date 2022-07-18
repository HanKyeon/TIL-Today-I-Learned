'''
n * n 크기의 정사각형 공간
a는 1,1에서 움직임 시작.
계획서는 L R U D로 적혀져 있음.
A가 공간을 벗어나는 이동은 무시된다.
최종 도착 지점의 좌표를 출력
N의 크기는 1~100 정수
이동할 계획서의 최대 len 100
'''
# 입력 받을 변수, 초기 위치
n = int(input())
x, y = 1, 1
plans = input().split()
# 이동의 종류와 이동에 따른 좌표이동을 순서대로 리스트에 정리
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 반복. plan이 plans 리스트를 쭉 훑는다.
for plan in plans :
    for i in range(len(move_types)) : # i가 move type의 인덱스를 훑을 때
        if plan == move_types[i] : # plans를 훑는 plan과 같은 종류의 이동을
            nx = x + dx[i] # 해
            ny = y + dy[i] # 준다
        if nx < 1 or ny < 1 or nx > n or ny > n : # 근데 벗어나면
            continue # 위치에 안넣을거다.
        x, y = nx, ny # 안벗어 났을 때 x, y에 newx, newy를 대입한다.

print (x, y) # 좌표 출력



