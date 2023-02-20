'''
영화감독 숌

666은 종말의 숫자다. 666이 1번 1666이 2번 해서 666이 연속으로 들어간 n번째 숫자를 구해라.

입력
n 제시.

출력
n번째 영화에 들어간 수 출력
'''
def check(num):
    while num > 665:
        if num%1000 == 666:
            return True
        num //= 10
    return False

n = int(input())
val = 665
while n:
    val += 1
    if check(val):
        n -= 1
print(val)

'''

# 빠른 코드

import sys

def how(n):
  if n%10==6: return 10*how(n//10)
  else: return 1

def getRes(first, mid, last, lst):
  print(first * 1000 * lst + mid * lst + last)
  sys.exit(0)

N = int(input())
first, mid, last, cnt = 0, 666, 0, 0

while cnt<N:
  idx = how(first)
  if idx > 1:
    for i in range(0, idx):
      cnt += 1
      if cnt == N:
        getRes(first // idx, mid, last, idx)
      last += 1
    last = 0
  else:
    cnt += 1
    if cnt == N:
      getRes(first, mid, last, idx)
  first += 1
'''

