'''
카드

카드 n장. -2**62 ~ 2**62
가장 많이 가지고 있는 정수를 구해라. 여러개라면 작은거

입력
n 제시
n개 줄 숫자 제시

출력
가장 많이 가진 정수 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
d = {}
for i in range(n) :
    num = int(input())
    if num in d: d[num]+=1; continue
    d[num] = 1

print(sorted(d.items(),key = lambda x : (-x[1],x[0]))[0][0])