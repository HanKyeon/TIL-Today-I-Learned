'''
골드바흐의 추측

4보다 모든 큰 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.

입력
n 계속 제시
0이면 종료

출력
n = a + b 형태로 출력
'''
import sys
input = sys.stdin.readline

che = [0,0]+[1]*999999
sosu = set()
for i in range(2, 1001):
    if not che[i]: continue
    for k in range(i+i,1000001,i): che[k] = 0
che[2] = 0
sosu = list(i for i, v in enumerate(che) if v)

while n:=int(input()):
    for i in sosu:
        if che[n-i]: print(f"{n} = {i} + {n-i}"); break


# sosu = [True] * 1000001
# m = int(1000001**0.5)
# for i in range(2,m+1):
#   if sosu[i]:
#     for k in range(i+i,1000001,i):
#       sosu[k] = False

# while True:
#   n = int(input())
#   if n==0:
#     break
#   else:
#     for i in range(2,m+3):
#       if sosu[i] and sosu[n-i]:
#         print("%d = %d + %d"%(n,i,n-i))
#         break




