'''
1, 2, 3 더하기

정수 n이 주어졌을 때 1, 2, 3의 합으로 나타내는 방법의 수
n은 양수이며 11보다 작다.
테케 주어짐

a 3개 b 4개로 주어진 총합 7개로 순서를 만드는 갯수는
7! / (3!*4!) 이다.

'''
import math

for _ in range(int(input())):
    n = int(input())
    cn = 0
    for k in range(n//3+1) :
        a = 3*k
        for j in range(n//2+1) :
            b =  2*j
            for i in range(n+1) :
                c = i
                if a+b+c == n :
                    cn += (math.factorial(k+i+j)) / ((math.factorial(k)) * (math.factorial(j)) * (math.factorial(i)))
    print(int(cn))

