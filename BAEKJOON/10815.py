'''
숫자 카드

숫자카드 n개 갖고 있음. m개 제시되었을 때, 가지고 있는지 아닌지 확인

입력
n 제시.
정수목록 제시
m 제시
보유 여부 확인.
'''
import sys
input = sys.stdin.readline

n, nl = int(input()), set(map(int, input().rstrip().split()))
m, ml = int(input()), list(map(int, input().rstrip().split()))
for i, v in enumerate(ml):
    if v in nl: ml[i] = 1
    else: ml[i] = 0

print(*ml)




