'''
대칭 차집합

자연수를 원소로 갖는 공집합이 아닌 두 집합 a, b
대칭 차집합의 원소 갯수 출력
a-b b-a의 합집합을 대칭 차집합이라 한다.

입력
a, b 갯수 제시
a
b

출력
대칭 차집합의 원소 갯수 출력
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a, b = set(map(int, input().rstrip().split())), set(map(int, input().rstrip().split()))
print(len(a-b)+len(b-a))

# 빠름
a,b,c=open(0)
a=(b+c).split()
print(2*len({*a})-len(a))
'''
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
cnt = 0
A = set(input().split())
for i in input().split():
    if i in A:
        cnt+=1
print(a+b-cnt*2)
'''

