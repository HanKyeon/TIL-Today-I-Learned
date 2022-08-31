'''
골드바흐의 추축

1보다 큰 자연수 중에서 1과 자기 자신을 제외한 약수가 없는 자연수를 소수라 한다.

2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이 골드바흐 수라고 한다.
짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램 작성. 골드바흐 파티션이 여러개일 경우 두 소수의 차이가 가장 작은 것을 출력.

입력
테케
짝수
짝수
짝수

출력
파티션
파티션
파티션
'''
# pypy 통과.

dp = [True] * 10001
dp[0], dp[1] = False, False
pn, i = [], 2
for i in range(2, 101):
    if dp[i]:
        pn.append(i)
        j = 2
        while i*j<=10000:
            dp[i*j] = False
            j += 1

for _ in range(int(input())):
    n = int(input())
    a, b = 0, 0
    for i in pn:
        if i <= n//2 and n-i in pn:
            a, b = i, n-i
        if i>n:
            break
    print(a, b)

'''
# 파이썬 패스 코드.
array = [True] * 10001
array[0] = False
array[1] = False
for i in range(2, int(len(array)**0.5)):
    if array[i] == True:
        for j in range(i+i, len(array),i):
            array[j] = False

for i in range(int(input())):
    a = int(input())
    
    b = a // 2
    c = b

    for _ in range(b+1):
        if array[b] == True and array[c] == True:
            print("{0} {1}".format(b,c))
            break
        b -=1
        c +=1
'''