'''
1059 좋은구간

정수집합 S
[A, B]

A와 B는 양의 정수
A<=x<=B 를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 갯수

첫째 줄에는 집합 S의 크기 L이 주어진다.
'''

l = int(input())
a = list(map(int, input().split())) # 이 때 a에 n이 있으면 바로 0 출력
n = int(input())

a.sort()

i = 0

while True :
    if (n in a) or (n > max(a)) :
        print('0')
        break
    else : 
        if a[0] > n : # 순서 중요하다. 예외적인 경우를 먼저 처리해주자..
            print(n * (a[0] - n) - 1)
            break
        if a[i] < n < a[i+1] :
            lef, rig = a[i], a[i+1]
            print((n-lef) * (rig - n) - 1)
            break
        i += 1

# n이 존재하는 a[x] < a[x+1] 사이의 값
# (n - a[x]) * (a[x+1] - n) - 1

