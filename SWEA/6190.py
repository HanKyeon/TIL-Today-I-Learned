'''
딱정곤의 단조 증가하는 수

단조 증가하는 수는 각 자릿수가 오른쪽으로 갈수록 증가하거나 같은 수.
양의 정수 N개 A1, AN이 주어진다.
1이상 i<j n이하 두 i, j에 대해 Ai*Aj값이 단조 증가하는 수인 것들을 구하고 그 중 최댓값

입력
테케
1이상 1000이하 정수
N개의 정수

출력
#T 단증수 최댓값.
단증수가 없으면
#T -1
'''
# 숫자를 받아 단조면 그대로 리턴, 아니면 -1 리턴
def danjoraise2(num) : #
    c = num
    ch = 9 # 10 나눗셈으로 계산하기 위해 반대로 1의 자리부터 확인해나간다.
    while c > 0 :
        if (c % 10) <= ch :
            ch = c % 10
            c = c // 10
            continue
        else :
            return (-1)
    return num
    
# 숫자를 받아 단조면 그대로 리턴, 아니면 -1 리턴
def danjoraise(num) :
    danjo = list(map(int,str(num)))
    ze = danjo[0]
    for i in range(len(danjo)):
        if ze <= danjo[i]:
            ze = danjo[i]
        else :
            return(-1)
    return num
# 몸체
for testcase in range(1, int(input())+1):
    # 입력
    n = int(input())
    nl = list(map(int, input().split()))
    maxval = -1 # 비교용 maxval
    for i in range(n) :
        for j in range(i+1, n) :
            maxval = max(maxval, danjoraise2(nl[i]*nl[j]))
    # 출력
    print(f"#{testcase} {maxval}")




