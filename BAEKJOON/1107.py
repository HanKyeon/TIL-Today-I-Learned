'''
리모컨

일부 **숫자**가 고장남.
리모컨 버튼이 0123456789 +- 존재. +는 +1 -는 -1
이동하려 하는 채널 N. 이동 할 때 버튼을 몇 번 눌러야 하는가?
현 채널 100

입력
이동하려는 채널 0이상 50만 이하.
고장난 버튼의 갯수 0이상 10이하
고장난 버튼 제시 (0이라면 생략)

출력
채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지 출력
'''

n = int(input())
m = int(input())

if m:
    gg = list(input().split()) 
    ans = abs(n-100)
    for i in range(1000001):
        num = str(i)
        for j in num:
            if gg and j in gg:
                break
        else:
            ans = min(ans, abs(i-n)+len(num))
    print(ans)
else:
    print(min((len(str(n))), abs(n-100)))

# 첫째 자리에서 가장 가까운 숫자 탐색

'''
1. 그리디하게 첫째 자리 선택.
1-1. 첫째자리가 작다면 뒷자리는 쭉 가장 큰 값
1-2. 첫째자리가 크다면 뒷자리는 쭉 가장 작은 값
1-3. 같다면 다음 자리에서 판단.
길이만큼 반복

마이너스에서 절댓값이 같은 값.
플러스에서 절댓값이 같은 값.
두 가지를 찾아서, 100번에서 이동하는 것과 min하여 계산.
'''


'''
        if fla1 == None or fla2 == None:
                
            if i==j:
                grc1 += j
                grc2 += j
                break
            elif i < j:
                chai = (ord(j)-ord(i))%10
                if 0 < chai < m:
                    m = chai
                    st2 = j
            elif i > j:
                chai = (ord(i)-ord(j))%10
                if 0 < chai < M:
                    M = chai
                    st1 = j
        if grc1[-1] == i:
            continue
        grc1 += st1
        grc2 += st2
    print(grc1, grc2)
'''













