'''
농작물 수확하기

N*N 농장.
1. N은 50이하 홀수
2. 수확은 정사각형에 딱 맞는 마름모 꼴.

입력
테케T
N
농장

출력
#T 농장 수익
'''
import sys
sys.stdin = open("input.txt", "r")

for testcase in range(1, int(input())+1):
    n = int(input())
    g=[list(map(int, input())) for _ in range(n)]
    t = list(range(n//2, 0, -1)) + list(range(n//2+1))
    sh = 0
    for i, j in zip(g, t) :
        sh += sum(i[j:n-j])
    print(f"#{testcase} {sh}")


