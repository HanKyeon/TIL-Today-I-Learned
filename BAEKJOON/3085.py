'''
사탕 게임

n*n 격차. 사탕 색이 다른 인접한 두 칸을 고른다. 고른 칸에 있는 사탕을 교환한다. 이후 가장 긴 연속 부분을 고르고 그 사탕을 모두 먹는다. 먹을 수 있는 최대 갯수 구하기.

입력
n 제시
n개 줄 그래프 제시 C P Z Y

출력
최대 갯수 출력
'''
import sys
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]
n = int(input())
g = [list(input().rstrip()) for _ in range(n)]
ans = 1

def lego(h, w):
    global ans
    nh, nw = h, 1
    cnt = 1
    while nw < n:
        if g[nh][nw] == g[nh][nw-1]:
            cnt += 1
            if ans < cnt:
                ans = cnt
        else:
            cnt = 1
        nw += 1
    nh, nw = 1, w
    cnt = 1
    while nh < n:
        if g[nh][nw] == g[nh-1][nw]:
            cnt += 1
            if ans < cnt:
                ans = cnt
        else:
            cnt = 1
        nh += 1

for h in range(n):
    for w in range(n):
        for dh, dw in [(1,0), (0,1)]:
            nh, nw = h+dh, w+dw
            if nh < n and nw < n:
                g[h][w], g[nh][nw] = g[nh][nw], g[h][w]
                lego(nh, nw)
                lego(h, w)
                g[h][w], g[nh][nw] = g[nh][nw], g[h][w]
print(ans)




'''
# 빠른 코드

import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    graph = [list(input().rstrip()) for _ in range(N)]
    total_max = 0
    for i in range(N):
        max_seq = [0, 0, 0]
        cur_seq = [0, 0, 0]
        prev_color = graph[i][0]
        is_connect = False
        for j in range(N):
            if graph[i][j] == prev_color:
                cur_seq[0] += 1
            else:
                cur_seq[2] = j
                front_connect = rear_connect = cur_seq[0]
                if not is_connect:
                    if cur_seq[1] > 0:
                        if (i > 0 and graph[i-1][cur_seq[1]-1] == prev_color) \
                            or (i < N-1 and graph[i+1][cur_seq[1]-1] == prev_color):
                            front_connect += 1
                        elif cur_seq[1]-1 > 0 and graph[i][cur_seq[1]-2] == prev_color:
                            front_connect += 1
                    
                    if j < N:
                        if (i > 0 and graph[i-1][j] == prev_color) \
                            or (i < N-1 and graph[i+1][j] == prev_color):
                            if j < N-1 and graph[i][j+1] == prev_color:
                                cur_seq[0] += 1
                                is_connect = True
                                continue
                            rear_connect += 1
                        elif j < N-1 and graph[i][j+1] == prev_color:
                            rear_connect += 1
                    
                    cur_seq[0] = max(front_connect, rear_connect)
                
                if cur_seq[0] > max_seq[0]:
                    max_seq = cur_seq[:]
                cur_seq = [1, j, j]
                prev_color = graph[i][j]
                is_connect = False
            
        if not is_connect:
            if cur_seq[1] > 0:
                if (i > 0 and graph[i-1][cur_seq[1]-1] == prev_color) \
                    or (i < N-1 and graph[i+1][cur_seq[1]-1] == prev_color):
                    cur_seq[0] += 1
                elif cur_seq[1]-1 > 0 and graph[i][cur_seq[1]-2] == prev_color:
                    cur_seq[0] += 1

        if cur_seq[0] > total_max:
            total_max = cur_seq[0]

        if max_seq[0] > total_max:
            total_max = max_seq[0]

    for j in range(N):
        max_seq = [0, 0, 0]
        cur_seq = [0, 0, 0]
        prev_color = graph[0][j]
        is_connect = False
        for i in range(N):
            if graph[i][j] == prev_color:
                cur_seq[0] += 1
            else:
                cur_seq[2] = i
                front_connect = rear_connect = cur_seq[0]
                if not is_connect:
                    if cur_seq[1] > 0:
                        if (j > 0 and graph[cur_seq[1]-1][j-1] == prev_color) \
                            or (j < N-1 and graph[cur_seq[1]-1][j+1] == prev_color):
                            front_connect += 1
                        elif cur_seq[1]-1 > 0 and graph[cur_seq[1]-2][j] == prev_color:
                            front_connect += 1
                    
                    if i < N:
                        if (j > 0 and graph[i][j-1] == prev_color) \
                            or (j < N-1 and graph[i][j+1] == prev_color):
                            if i < N-1 and graph[i+1][j] == prev_color:
                                cur_seq[0] += 1
                                is_connect = True
                                continue
                            rear_connect += 1
                        elif i < N-1 and graph[i+1][j] == prev_color:
                            rear_connect += 1
                    
                    cur_seq[0] = max(front_connect, rear_connect)

                if cur_seq[0] > max_seq[0]:
                    max_seq = cur_seq[:]
                cur_seq = [1, i, i]
                prev_color = graph[i][j]
                is_connect = False

        if not is_connect:
            if cur_seq[1] > 0:
                if (j > 0 and graph[cur_seq[1]-1][j-1] == prev_color) \
                    or (j < N-1 and graph[cur_seq[1]-1][j+1] == prev_color):
                    cur_seq[0] += 1
                elif cur_seq[1]-1 > 0 and graph[cur_seq[1]-2][j] == prev_color:
                    cur_seq[0] += 1
        
        if cur_seq[0] > total_max:
            total_max = cur_seq[0]

        if max_seq[0] > total_max:
            total_max = max_seq[0]
                
    print(total_max)


if __name__=='__main__':
    main()
'''

'''
# 빠른 코드 2

import sys
input = sys.stdin.readline

def explore(board):
    global n

    uni = 0
    res = 0
    for i in range(n):
        if board[i] == board[i][0] * n:
            if uni == 0:
                uni += 1
                res = max(res, n-1)
                continue
            else:
                res = n
                break
        chance = 1
        cnt = 0
        candy = ''
        for j in range(n):
            if cnt == 0:
                candy = board[i][j]
                cnt += 1
                res = max(res, cnt)
            else:
                if board[i][j] == candy:
                    cnt += 1
                    res = max(res, cnt)
                else:
                    if chance:
                        for dy in [-1, 1]:
                            ny = i + dy
                            if 0 <= ny < n and board[ny][j] == candy:
                                chance = 0
                                cnt += 1
                                res = max(res, cnt)
                                break
                        else:
                            if j + 1 < n and board[i][j+1] == candy:
                                cnt += 1
                                res = max(res, cnt)
                            cnt = 1
                            candy = board[i][j]
                    else:
                        cnt = 1
                        candy = board[i][j]
                        chance = 1
    return res

def swap(board):
    turn_board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            turn_board[i][j] = board[n-1-j][i]
    return turn_board


n = int(input())
matrix = [list(input().rstrip()) for _ in range(n)]
ans = []

for _ in range(4):
    ans.append(explore(matrix))
    matrix = swap(matrix)
print(max(ans))
'''

