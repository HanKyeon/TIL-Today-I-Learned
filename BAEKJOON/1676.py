'''
팩토리얼 0의 갯수

N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때 까지의 0의 갯수
'''
from math import factorial

n = int(input())
a = factorial(n)
a = str(a)
c = 0
for i in range(len(a)-1, -1, -1):
    if a[i] == '0':
        c += 1
    else:
        break
print(c)