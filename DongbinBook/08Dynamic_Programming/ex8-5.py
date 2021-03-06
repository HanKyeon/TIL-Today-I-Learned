'''
1. 5로 나눠지면 5로 나눈다.
2. 3으로 나누어 떨어지면 3으로 나눈다.
3. 2로 나눠지면 2로 나눈다.
4. 1을 뺀다.

숫자가 주어졌을 때, 해당 4개의 방법을 이용해 최단으로 1이 되도록 만들 때 필요한 연산 횟수.
입력해주는 정수 x는 1에서 3만 사이 임의의 값
'''
# 입력
x = int(input())
# dp 테이블 생성. x는 1부터 30000 사이의 값. 값에 따라 얼마나 걸릴지 계산해서 넣어둘 테이블
d = [0] * 30001
# bottom up 방식
for i in range(2, x+1) :
    # 현재 수에서 1을 빼는 경우, 이전 항의 값에서 횟수를 1회 더 한다.
    # 동시에, d[i] 값 초기화도 해준다.
    d[i] = d[i - 1] + 1

    # 2로 나누어지면 2배 값이 나오는 횟수에서 1번 더 행한 것과 같다.
    # 기존 값과 비교하여 작은 값을 넣는다.
    if i % 2 == 0 :
        d[i] = min(d[i], d[i // 2] + 1)
    # 3으로 나눠지면 동일
    if i % 3 == 0 :
        d[i] = min(d[i], d[i // 3] + 1)
    # 5로 나눠지면 동일
    if i % 5 == 0 :
        d[i] = min(d[i], d[i // 5] +1)
# dp 테이블에 계싼된 횟수를 출력해준다.
print(d[x])





