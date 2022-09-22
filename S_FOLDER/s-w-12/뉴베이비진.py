'''
베이비 진

연속 3개이상 run
같은 숫자 3개 이상 triplet
플1 플2 교대로 한 장씩. 6장 전에 run이나 triplet 되면 승리.
12장 카드 주었을 때, 승자 누구임?

입력
테케T
숫자

출력
#테케 무승부0 1승 1 2승2
'''
def check(li):
    if len(li) < 3:
        return False
    wit = [0]*10
    for i in li:
        wit[i]+=1
    k = 0
    while k < 10:
        if wit[k] == 0:
            k+=1
            continue
        if wit[k]==3:
            return True
        if sum(wit[k:k+3]) >= 3 and 0 not in wit[k:k+3]:
            return True
        k+=1
    return False

for tc in range(1, int(input())+1):
    nl = list(map(int, input().rstrip().split()))
    p1, p2 = [], []
    for i in range(12):
        if i % 2:
            p2.append(nl[i])
            if check(p2):
                print(f"#{tc} 2")
                break
        else:
            p1.append(nl[i])
            if check(p1):
                print(f"#{tc} 1")
                break
    else:
        print(f"#{tc} 0")







