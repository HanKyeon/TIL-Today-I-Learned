'''
곱셈

자연수 A를 B번 곱한 수를 C로 나눈 나머지
'''
# 잘 모르겠어서 해결 방법 찾아봄

def power(a, b):
    if b == 1:
        return a % C
    else:
        temp = power(a, b // 2)
        if b % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * a % C

A, B, C = map(int, input().split())
result = power(A, B)
print(result)