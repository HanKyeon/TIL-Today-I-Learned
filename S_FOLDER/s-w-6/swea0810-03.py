'''
회전~~ 회오리~~~ 슈우우웃~
'''

# 재귀. 인자로는 x,y 좌표, 들어가는 상자 길이, startnumber.
def circle(x, y, l, stan) :
    # 종료조건
    if l == 1: # 길이 1이면 채우고 끝
        g[x][y] = stan
        return
    if l == 0 : # 길이 0이면 그냥 끝
        return
    # 숫자 칠하기. 테두리 칠하고 내부 박스로 넘겨주는 방식
    for i in range(l-1) : # 가로칠
        g[x][y + i] = stan
        stan += 1
    for j in range(l-1) : # 오른쪽 세로칠
        g[x + j][y+l-1] = stan
        stan += 1
    for k in range(l-1) : # 아래칠
        g[x+l-1][y+l-1-k] = stan
        stan += 1
    for p in range(l-1) : # 왼쪽 세로칠
        g[x+l-1-p][y] = stan
        stan += 1
    # 테두리를 칠했다면 같은 작업을 x+1, y+1에 l-2 길이의 박스에 현재 숫자를 들고 가면
    # 끝날 때까지 재귀함.
    return circle(x+1, y+1, l-2, stan)

for testcase in range(1, int(input())+1) :
    n = int(input())
    g = [[1]*n for _ in range(n)]
    circle(0, 0, n, 1)
    print(f"#{testcase}")
    for i in range(n) :
        print(*g[i])


