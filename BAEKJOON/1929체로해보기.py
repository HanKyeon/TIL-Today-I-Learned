'''
소수 구하기
'''
# 입력 받기
m, n = map(int,(input().split()))
# m이 1이면 2부터 시작
if m == 1 :
    m = 2
# m부터 n까지 순회하면서
for i in range(m, n+1) :
    # i의 제곱근까지만 확인
    for j in range(2, int(i ** (1/2)) + 1):
        if i % j==0: # 나눠지면 끝
            break
    else: # 소수면 출력
        print(i)

'''
시간나면 에라토스 뭐시깽의 체 한 번 해보자.
'''