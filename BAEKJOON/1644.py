'''
소수의 연속합

하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다.
연속된 소수 합으로 나타낼 수 없는 자연수가 존재. 20이 예시. 7+13으로 표현이 가능하나 연속 소수가 아님. 소수느 ㄴ한 번만 덧셈에 사용 가능.
자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램 작성.

입력
자연수 N 제시. 1이상 400만 이하.

출력
자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수.
'''

n = int(input())

v = [1] * (n+1)
v[0], v[1] = 0, 0
for i in range(2, n+1):
    if v[i]:
        j = 2
        while i*j<=n:
            v[i*j] = 0
            j+=1
pn = [i for i, va in enumerate(v) if va == 1]

for i in range(len(pn)):
    val = pn[i]
    for j in range(i+1, len(pn)):
        if val + pn[j] > n:
            break
        val += pn[j]
        v[val] += 1

print(v[n])




