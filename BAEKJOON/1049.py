'''
기타줄

기타에서 n개 줄이 끊김. 6줄 패키지, 1개이상 줄은 낱개 구매 가능

입력
n, m 제시.
m개 줄 패키지 가격, 낱개 가격 제시

출력
n개 사기 위해 필요한 돈의 최솟값 출력
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
pm, nm = 1111, 1111
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    if pm > a: pm = a
    if nm > b: nm = b
if pm > nm*6: print(nm*n)
else: print(n//6*pm + (n%6*nm if n%6*nm < pm else pm))

