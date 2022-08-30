'''
종이의 개수

n*n 행렬 종이. -1 0 1 중 하나.
1. 종이가 모두 같은 수라면 종이 그대로 사용.
2. 종이가 모두 같은 수가 아니라면, 9개로 자르고, 잘린 종이에 대해 1을 반복.
이렇게 진행 했을 때, -1로만 채워진 종이의 갯수, 0으로만 채워진 종이의 갯수, 1로만 채워진 종이의 갯수를 구하는 프로그램 작성.

입력
1이상 3**7 이하 n. n은 3의 n승꼴. 2187이하.
행렬 제시

출력
-1로 채워진 종이 갯수
0으로 채워진 종이 갯수
1로만 채워진 종이 갯수

'''
import sys
input = sys.stdin.readline

def cp(h, w, ln):
    global di
    b = g[h][w]
    if ln == 1: # 길이 1이면
        di[b] += 1 # 딕트 그 값에 1 추가
        return
    
    fla = True
    for i in range(h, h+ln): # 받은 범위 탐색
        for j in range(w, w+ln):
            if g[i][j] != b: # 값이 b와 달라지는게 있으면 돔황챠
                fla = False
                break
        if fla == False: # 돔황챴으면 이 for문도 돔황챠
            break
    if fla: # 그래도 True면
        di[b] += 1 # 딕트에 하나 올리고
        return # 끝
    else: # 아니면
        nln = ln//3 # 9개로 쪼개서
        for i in range(0, ln, nln): # 더해주는 식이니까 0시작 해야함!
            for j in range(0, ln, nln): # 마찬가지!
                cp(h+i, w+j, nln) # 종이 자르기
# 입력
n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]

di = {-1:0, 0:0, 1:0}
cp(0, 0, n)
# 출력
print(di[-1])
print(di[0])
print(di[1])






