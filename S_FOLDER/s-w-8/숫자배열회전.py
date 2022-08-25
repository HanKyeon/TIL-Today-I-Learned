'''
숫자 배열 회전

시계 방향으로 90도 180도 270도 회전한 모양 출력

입력
테케T
N
행렬

출력
#T
90도1 180도1 270도1
90도2 180도2 270도2
'''
def h90(g):
    global n
    s = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s[i][j] = g[n-j-1][i]
    return s

for testcase in range(1, int(input())+1):
    n = int(input())
    g = [list(input().split()) for _ in range(n)]
    g90 = h90(g)
    g180 = h90(g90)
    g270 = h90(g180)
    print(f"#{testcase}")
    for i in range(n):
        ans = ''
        ans += ''.join(g90[i]) + ' '
        ans += ''.join(g180[i]) + ' '
        ans += ''.join(g270[i])
        print(ans)


