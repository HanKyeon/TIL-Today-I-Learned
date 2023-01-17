'''
돌 게임

탁자 위 n개의 돌.
돌을 1개 또는 3개 가져갈 수 있다.
마지막 돌을 가져가는 사람이 게임을 이기게 된다.
환벽히 게임 했을 때, 이기는 사람을 구해라. 상근이가 먼저함.

입력
n

출력
상근이가 이기면 SK 창영이가 이기면 CY
'''
def lego(num):
    if num%2:
        return "SK"
    return "CY"
n = int(input())
print(lego(n))




