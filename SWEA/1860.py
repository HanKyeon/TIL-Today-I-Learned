'''
진기의 붕어빵

N명의 사람
0초부터 붕어빵 시작
M초동안 K개
지연시간 없이 제작 가능
0초 이후 손님이 언제 도착하는지 주어지면 모두에게 붕어빵을 노쿨로 줄 수 있는지 판별

입력
테케
1이상 100이하 N손님수 M제작시간 K갯수
N개의 정수가 공백으로 도착시간 초단위 0~ 11111

출력
#T Possible
#T Impossible
'''

for testcase in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    tl = list(map(int, input().split()))
    dp = [0] * 11112
    c, ans = 0, 'Possible'
    for i in range(11112):
        if i % m == 0 and i != 0:
            c += k
        if i in tl:
            c -= 1
        if c < 0:
            ans = 'Impossible'
            break
    print(f"#{testcase} {ans}")
