'''
경사로

n n 지도. 높이 제시.
높이가 모두 같거나, 경사로를 놓아서 지나갈 수 있어야 한다. 경사로는 높이가 항상 1, 길이는 L

경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로 바닥이 모두 접해야 한다.
낮은 칸과 높은 칸의 차이가 1이어야 한다.
경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.

경사로를 놓은 곳에 또 경사로를 놓는 경우
낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
경사로를 놓다가 범위를 벗어나는 경우

지도가 주어졌을 때, 지나갈 수 있는 길의 갯수를 구해라.

입력
2이상 100이하 n 1이상 n이하 L 제시.
지도 제시. 각 칸의 높이는 10이하 자연수

출력
지나갈 수 있는 길의 갯수.
'''
import sys
input = sys.stdin.readline

n, l = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
s = list(map(list, zip(*g)))
ans = 0
for i in range(n):
    gsta, ssta = [], [] # 가로 스택, 세로 스택
    oru1, oru2 = True, True
    fla1, fla2 = True, True
    for j in range(n):
        if fla1: # 계속 맞는 길만 걸어왔다면
            if not oru1: # 내리막길이고
                if len(gsta) == l: # 경사로가 확보 되었으면
                    if gsta[-1] == g[i][j]: # 다음꺼랑 높이가 같다면
                        gsta = [] # 경사로 넣어준다. 빈 칸이면 뒤에서 g[i][j]를 넣어줄 것
                        oru1 = True # 오르막길로 바꿔줌. (표준으로 변경)
                    elif gsta[-1] + 1 == g[i][j]: # 다음꺼가 오르막이면
                        fla1 = False # 못한다.
                    elif gsta[-1] - 1 == g[i][j]: # 하나 더 내리막이면
                        gsta = [] # 초기화만 해준다. 없으면 저기서 넣어줄 것
            if not gsta: # 빈 배열이라면 넣어준다.
                gsta.append(g[i][j])
            elif gsta and gsta[-1] == g[i][j]: # 배열이 있고 뒤와 같다면 추가해준다.
                gsta.append(g[i][j])
            elif gsta and gsta[-1] + 1 == g[i][j]: # 오르막길이라면
                if not oru1: # 내리막길 중에 오르막 나왔으면
                    fla1 = False # 안된다.
                oru1 = True # 오르막길 표시
                if len(gsta) >= l: # 경사로 확보 되었다면
                    gsta = [g[i][j]] # 하나 넣고 새로 시작
                elif len(gsta) < l:
                    fla1 = False
            elif gsta and gsta[-1] - 1 == g[i][j]: # 한 칸 내리막길이라면
                if not oru1: # 내리막길 중에 내리막 나왔으면
                    fla1 = False
                oru1 = False # 내리막길임을 명시
                gsta = [g[i][j]] # 새로 시작해줌.
            else: # 차이가 2 이상이면 경사로를 둘 수 없다.
                fla1 = False

        if fla2:
            if not oru2: # 내리막길이고
                if len(ssta) == l: # 길이 확보 되었으면
                    if ssta[-1] == s[i][j]: # 다음꺼랑 높이가 같다면
                        ssta = [] # 경사로 넣어준다.
                        oru2 = True # 오르막길로 바꿔줌.
                    elif ssta[-1] + 1 == s[i][j]: # 다음꺼가 오르막이면
                        fla2 = False # 못한다.
                    elif ssta[-1] - 1 == s[i][j]: # 하나 더 내리막이면
                        ssta = [] # 초기화만 해준다. 없으면 저기서 넣어줄 것
            if not ssta:
                ssta.append(s[i][j])
            elif ssta and ssta[-1] == s[i][j]:
                ssta.append(s[i][j])
            elif ssta and ssta[-1] + 1 == s[i][j]: # 오르막길이라면
                if not oru2: # 내리막길 중에 오르막 나왔으면
                    fla2 = False
                oru2 = True # 오르막길 표시
                if len(ssta) >= l: # 경사로 확보 되었다면
                    ssta = [s[i][j]] # 하나 넣고 새로 시작
                elif len(ssta) < l:
                    fla2 = False
            elif ssta and ssta[-1] - 1 == s[i][j]: # 한 칸 내리막길이라면
                if not oru2: # 내리막길 중에 내리막 나왔으면
                    fla2 = False
                oru2 = False # 내리막길임을 명시
                ssta = [s[i][j]] # 새로 시작해줌.
            else:
                fla2 = False
    if not oru1: # 내리막길이고
        if len(gsta) == l: # 길이 확보 되었으면
            pass # 패스
        else: # 확보 못했으면 정답 아님
            fla1 = False
    if not oru2: # 내리막길이고
        if len(ssta) == l: # 길이 확보 되었으면
            pass # 패스
        else: # 확보 못했으면 구라
            fla2 = False
    if fla1:
        # print(f"{i}번째 가로 줄 가능")
        ans += 1
    if fla2:
        # print(f"{i}번째 세로 줄 가능")
        ans += 1
print(ans)


















