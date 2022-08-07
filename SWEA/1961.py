'''
숫자 배열 회전

N*N 배열을 90도 180도 270도 회전한 모양 출력
N은 3이상 7이하

입력
테케 갯수
3이상 7이하 N
행렬

출력
#1 #2 #3 \n
다음에 회전한 모양 출력
90도1행 180도1행 270도 1행
90도2행 180도2행 270도 2행
이런식으로
'''
# 90도 돌리기
def turn90(g) :
    l = len(g)
    g9 = [[0] * n for _ in range(n)]
    for i in range(l) :
        for j in range(l) :
            g9[i][j] = g[l-1-j][i]
    return g9

# testcase!!!!!!!!!!!!!!!!! testcase!!!!!!!!!!!!!!!!
for testcase in range(1, int(input())+1) :
    #입력
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    #돌리기
    g90 = turn90(g)
    g180 = turn90(g90)
    g270 = turn90(g180)
    # 출력
    print(f"#{testcase}")
    for i in range(n):
        for a in range(n):
            print(g90[i][a], end='')
        print(end=' ')
        for b in range(n):
            print(g180[i][b], end='')
        print(end=' ')
        for c in range(n):
            print(g270[i][c], end='')
        print()
    
    '''    for a, b, c in g90, g180, g270 :
        print(''.join(map(str, a)), end=' ')
        print(''.join(map(str, b)), end=' ')
        print(''.join(map(str, c)))
    '''



