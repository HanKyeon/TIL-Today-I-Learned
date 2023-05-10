'''
누울 자리를 찾아라

정사각형, 벽. 편하게 누울 수 있엉 ㅑ함. 연속 2칸 이상의 빈 칸이 존재하면 됨. 가로세로. 전체로 보는 듯.

입력
n 제시.
n개 줄 그래프
.은 빈 칸 X는 안됨

출력
가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리 갯수 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
g = [list(map(lambda x: 0 if x == '.' else 1, list(input().rstrip()))) for _ in range(n)]
s = list(map(list, zip(*g)))
garo, sero = 0, 0
for i in g:
    cnt = 0
    for j in range(n):
        if i[j] == 1:
            if cnt > 1:
                garo += 1
            cnt = 0
            continue
        cnt += 1
    if cnt > 1:
        garo+=1
for i in s:
    cnt = 0
    for j in range(n):
        if i[j]:
            if cnt > 1:
                sero += 1
            cnt = 0
            continue
        cnt += 1
    if cnt > 1:
        sero+=1
print(garo, sero)