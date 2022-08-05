'''
주사위 쌓기

마주 본 숫자 합 1 아님.
A-F B-D C-E 끼리 마주봄
각 각 쌓았을 때 최댓값은
max(b,c,d,e) max(a,c,e,f) max(a,b,d,f)
쌓을 때 같은 숫자끼리 마주봐야 함.

인덱스로 보자면
0-5 1-3 2-4
1234 0245 0135

입력
n은 만개 이하 자연수
A B C D E F n번 제시
'''
# ABCDEF를 012345로 보고 제작.
import sys
sys.setrecursionlimit(10**7)
n = int(input())
dices = []
for _ in range(n) :
    dices.append(list(map(int, input().split())))
# 파라미터는 맞춰야 할 아랫번호, 주사위 디자인, 종료조건 주사위 갯수 카운트용
def dice(upper_num, dice_design, dicenum) :
    idx = dice_design.index(upper_num)
    maxval = 0
    dn=dicenum
    # 종료 조건 주사위 다 하면 끝낸다.
    if dicenum == len(dices) :
        if idx == 0 or idx == 5 :
            maxval = max(dice_design[1], dice_design[2], dice_design[3], dice_design[4])
            return maxval
        elif idx == 1 or idx == 3 :
            maxval += max(dice_design[0], dice_design[2], dice_design[4], dice_design[5])
            return maxval
        elif idx == 2 or idx == 4 :
            maxval += max(dice_design[0], dice_design[1], dice_design[3], dice_design[5])
            return maxval
    
    # 0이나 5에 있을 때
    if idx == 0 or idx == 5 :
        maxval = max(dice_design[1], dice_design[2], dice_design[3], dice_design[4])
        if idx == 0 :
            u = dice_design[5]
        else :
            u = dice_design[0]
        return maxval + dice(u, dices[dicenum], dicenum+1)
    # 1이나 3에 있을 때
    elif idx == 1 or idx == 3 :
        maxval += max(dice_design[0], dice_design[2], dice_design[4], dice_design[5])
        if idx == 1:
            u = dice_design[3]
        else :
            u = dice_design[1]
        return maxval + dice(u, dices[dn], dn+1)
    # 2나 4에 있을 때
    elif idx == 2 or idx == 4 :
        maxval += max(dice_design[0], dice_design[1], dice_design[3], dice_design[5])
        if idx == 2 :
            u = dice_design[4]
        else :
            u = dice_design[2]
        return maxval + dice(u, dices[dicenum], dicenum+1)

# 최댓값 출력
print(max(dice(1, dices[0], 1), dice(2, dices[0], 1), dice(3, dices[0], 1), dice(4, dices[0], 1), dice(5, dices[0], 1), dice(6, dices[0], 1)))
