'''
보기만해도 쓰러질거 같은 문젠데 이게 별 두개야 왜???/ 40분밖에 안줘?????

n*m 직사각형. 육지 또는 바다. 육지만 이동 가능 바다 이동 불가.
캐릭터 시작 위치, 바라보는 위치. 움직이는건 아래 조건
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 왼쪽에 가보지 않은 땅이 있다면 왼쪽으로 회전 후 1칸 전진.
   만약 가보지 않은 칸이 없다면, 왼쪽으로 회전만.
3. 네 방향 모두 이미 가본 칸이거나 바다로 되어 있을 경우, 바라보는 방향을 유지 한 채
   한 칸 후진 한 뒤 1로 되돌아감. 이 때 뒤쪽이 바다라면 움직임 정지.

입력은 맵 크기
캐릭터 위치 및 방향
이후 맵을 받음
북동남서 순서로 0123
'''

# 맵 크기
n, m = map(int, input().split())
# 방문 위치와 바다를 tf로 표현하기 위해 전부 다 0으로 초기화
d = [[0] * m for _ in range(n)]
# 캐릭터 위치, 바라보고 있는 방향
x, y, direction = map(int, input().split())
d[x][y] = 1
# 맵 입력 받기
array = []
for i in range(n) :
    array.append(list(map(int, input().split())))
# 북 동 남 서 (0123) 방향 정리
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 왼쪽으로 회전만
def turn_left():
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3
# 시작
count = 1 # 
turn_time = 0 # 이건 4번 돌면 갈 곳 없다 판단하기 위함.

while True :
    turn_left() #일단 돌고 전진 여부 결정
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 한 이후 일단 전진. 이후 정면에 가보지 않은 칸이 있으면 대입.
    #  1이면 대입 안한다. 못가거나 가본 곳이 1이니까.
    if d[nx][ny] == 0 and array[nx][ny] ==0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 가본 곳이면 아까 돌았으니까 돌기 카운트 올리기만 해
    else : 
        turn_time += 1
    # 4번 돌았으면 갈 곳이 없는거니까 바라본 방향의 반대로 가
    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 거기가 땅이라면 거기가 최종 위치야.
        if array[nx][ny] == 0 :
            x = nx
            y = ny
        else : # 바다거나 못가면 끝내 그냥
            break
        # 다시 돌아야 하니 0으로 초기화해
        turn_time = 0

print(count) # 출력



