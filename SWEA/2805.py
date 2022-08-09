'''
농작물 수확하기

N*N 농장.
마름모꼴만 수확.
N은 항상 홀수
수확은 정사각형 마름모 형태만 가능.

입력
T 입력
농장 그래프 입력

출력
#t 수확 수
'''
# 테케
for testcase in range(1, int(input()) + 1) :
    # 입력
    n = int(input())
    m = n // 2 # 중앙값
    farm = [list(map(int, input())) for _ in range(n)]
    rfarm = list(range(m)) + list(range(m, -1, -1)) # 양쪽에서 빠지는 그래프
    val = 0
    # 실행
    for i in range(n) :
        val += sum(farm[i][m-rfarm[i]:m+rfarm[i]+1])
    #출력
    print(f"#{testcase} {val}")