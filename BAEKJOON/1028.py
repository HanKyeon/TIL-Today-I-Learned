'''
다이아몬드 광산

0과 1로 이루어진 R행 C열 배열.
따이아는 1로 이루어진 마름모 꼴.
가장 큰 다이아 크기 출력.

입력
r, c 제시. 750이하 자연수
r개 줄 그래프

출력
크기가 가장 큰 다이아 크기 출력. 없다면 0 출력
'''
import sys
input = sys.stdin.readline

def checkDp(h, w):
    global n, m, ans, md
    uph, upw, downh, downw = h, w, h, w
    while 0<=uph<n and 0<=upw<m and 0<=downh<n and 0<=downw<m and g[uph][upw] and g[downh][downw]:
        dp[h][w]+=1
        uph, upw, downh, downw = uph-1, upw+1, downh+1, downw+1
    uph, upw, downh, downw = h, w, h, w
    while 0<=uph<n and 0<=upw<m and 0<=downh<n and 0<=downw<m and g[uph][upw] and g[downh][downw]:
        uph, upw, downh, downw = uph-1, upw-1, downh+1, downw-1
        dp2[h][w]+=1
        if 0<=w-dp2[h][w]*2+2 and dp[h][w-dp2[h][w]*2+2] >= dp2[h][w] and ans < dp2[h][w]:
            ans = dp2[h][w]

n, m = map(int, input().rstrip().split())
g = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp2 = [[0]*m for _ in range(n)]
md =m if m < n else n
ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j]:
            checkDp(i, j)

print(ans)

'''
# 짱 빠른 코드

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]
ld = [[0 for _ in range(C)] for _ in range(R)]
rd = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R-1, -1, -1):
    for j in range(C):
        if arr[i][j] == '0':
            continue
        if i+1 < R and j-1 >= 0:
            ld[i][j] = ld[i+1][j-1] + 1
        else:
            ld[i][j] = 1
        if i+1 < R and j+1 < C:
            rd[i][j] = rd[i+1][j+1] + 1
        else:
            rd[i][j] = 1

ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == '0':
            continue
        min_value = min(ld[i][j], rd[i][j])
        if min_value < ans:
            continue
        for k in range(min_value, 0 , -1):
            if ld[i+k-1][j+k-1] >= k and rd[i+k-1][j-(k-1)] >= k:
                ans = max(ans, k)
                break
print(ans)
'''

'''
3
2
0
2
3
1
1
1
1
2
6
1
1
2

4 4
1111
1111
1111
1111

11 11
11111111111
11110111111
11111111111
11111111111
11111111111
11111111111
11111111111
11111111111
11111111111
11110111111
11111111111
답 : 5

11 11
11111111111
11111111111
11111111111
11111111111
11111111111
11111111111
11111111111
11111111111
11111111111
11111111111
11111111111

9 14
00000000000000
01000000010000
00100000101001
00000001000101
00001010000110
00000100001100
00000010011000
00000001110000
00000000100000
답 : 1

4 7
0001000
0010100
0101010
1000000

9 9
001000100
000101000
000010000
000101000
001000100
000101000
000010000
000101000
001000100
정답 3

9 9
010001000
001010000
000100000
001010000
010001000
001010000
000100000
001010000
010001000
정답 3

9 9
001000100
000101000
000010000
000001000
001000100
000101000
000010000
000101000
001000100
정답 1

8 8
11101111
11100111
10111111
11011111
11111111
11110111
11111111
11110110
정답 : 3
'''










