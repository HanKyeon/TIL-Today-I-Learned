'''
언더 프라임 * 파이파이 시간부족

X를 소인수분해 하면 곱해서 X가 되는 소수의 목록을 얻을 수 있다.
어떤 수 X를 소인수분해해서 구한 소수 목록의 길이가 소수이면 그 수는 언더프라임.
예시로 12는 2 2 3으로 길이가 3이므로 언더프라임이다.
두 정수 A, B가 주어졌을 때, A보다 크거나 같고, B보다 작거나 같은 정수 중에서
언더프라임인 수의 갯수를 구하자.

입력
A B

출력
A이상 B이하 언더프라임 갯수 출력
2이상 10만 이하 정수이다. A보다 B가 더 큼.
2 3 5 7 9

9제곱

길이가 16이하인 곱으로 나타내지면 된다.
2 3 5 7 11 13
'''

# 입력
a, b = map(int, input().split())
dp = [1] * (b//2+1) # 적어도 2개 이상의 소수곱이어야 하므로 b//2까지의 소수만 구하면 됨
dp[0], dp[1] = 0, 0 # 0과 1 초기화
for i in range(2, len(dp)): # 에라토스테네스의 체로 소수 구하기
    if dp[i] == 1:
        j = 2
        while i*j <= len(dp)-1:
            dp[i*j] = 0
            j += 1
pns = [i for i, v in enumerate(dp) if v == 1] # 소수 리스트
dp += [0] * (b//2+1) # b까지의 데이터를 받기 위해 늘려줌.
# b까지 작업한다. k // i보다 1번 더 곱해진 것이므로
for i in range(b+1): # b까지 작업
    for k in pns: # 5만 이하 소수 순회
        if k < i and i % k == 0: # 자기보다 작고 나뉘면
            dp[i] = dp[i//k] + 1 # i//k보다 1 하나 더 큼
            # 이 때 여러번 나뉘는 경우는 i가 올라가기 전에 처리되므로 상관 없음.
            # 예시로, dp[4]가 먼저 dp[2]+1 되서 2가 된 상태로 dp[8]을 확인하기에
            # dp[8]은 dp[4]+1이 된다.
c = 0 # 갯수
for i in range(a, b+1): # 슬라이싱으로 하려다 오래걸릴거 같아서 순회로 변경.
    if dp[i] in pns:
        c+=1
print(c)


'''
파이썬으로 맞춘 아저씨 se5674

result=0 
for k in range(a,b+1):
    if primenumber[k]==False:
        divnum=2
        cnt=0
        while True:
            if k%divnum==0:
                cnt+=1
                k//=divnum
                if primenumber[k]==True:
                    cnt+=1
                    break
                
            else:
                divnum+=1
        if primenumber[cnt]==True:
            result+=1            
        
print(result)        

'''







