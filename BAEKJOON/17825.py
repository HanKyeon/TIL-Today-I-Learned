'''
주사위 윷놀이

처음 시작 칸 말 4개
말은 화살표 방향으로만 이동 가능.
파란칸에서는 파란 화살표 우선
말의 이동을 마치는 칸에 다른 말이 있다면 그 말은 이동 불가. 단, 도착 칸으로 이동이면 가능.
말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가.
주사위에서 나올 수 10개를 미리 알고 있을 때, 얻을 수 있는 점수의 최댓값.

입력
주사위에서 나올 수 10개 순서대로 제시.

출력
얻을 수 있는 점수 최댓값 출력.
'''
'''
말판 짜다가 검색했음.
'''
import sys
input = sys.stdin.readline

pan = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
nl = list(map(int, input().split()))
ans = 0
def dfs(idx:int, points:int, mal:list, stk:list):
    global ans
    if idx >= 10:
        ans = max(ans, points)
        return
    for i in range(4):
        x = mal[i]
        if len(pan[x]) == 2:
            x = pan[x][1]
        else:
            x = pan[x][0]
        for j in range(1, nl[idx]):
            x = pan[x][0]
        if x == 32 or (x < 32 and x not in mal):
            before = mal[i]
            mal[i] = x
            stk.append(x)
            dfs(idx + 1, points+score[x],mal, stk)
            stk.pop()
            mal[i] = before
dfs(0, 0, [0,0,0,0], [])
print(ans)














