'''
상하좌우
'''
# LRUD
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
dr = ["L", "R", "U", "D"]
x, y = 0, 0
# n,n 벗어나면 무시.

n = int(input())
d = list(input().split())

for i in d :
    for j in dr :
        if i == j :
            nx = x + dx[dr.index(j)]
            ny = y + dy[dr.index(j)]
    
    if 0 <= nx < n and 0<= ny < n :
        x, y = nx, ny

print(x+1, y+1)


''' 
먼저 만들어 본 코드이나 줄일 수 있다... 4방향 뿐이라 아래처럼 하는게 더 빠르지 않을까?

    if i == "L" :
        nx = x + dx[0]
        ny = y + dy[0]
    if i == "R" :
        nx = x + dx[1]
        ny = y + dy[1]
    if i == "U" :
        nx = x + dx[2]
        ny = y + dy[2]
    if i == "D" :
        nx = x + dx[3]
        ny = y + dy[3]
'''