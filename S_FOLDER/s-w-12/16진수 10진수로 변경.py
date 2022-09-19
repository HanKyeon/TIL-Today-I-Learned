'''
16진수 숫자를 7비트로 묶어 십진수로 변환.
'''
b = [64,32,16,8,4,2,1]
for tc in range(1, int(input())+1):
    a = input() # 입력
    la = len(a) # 16진수 길이
    s = bin(int(a, 16))[2:] # 2진수
    while len(s) != la*4: # 16진수 길이*4가 아니라면
        s = '0'+s # 앞에 0을 그만치 붙여준다.
    print(f"#{tc}", end=' ') # 테케 출력
    for i in range(0, len(s), 7): # 길이 7로 확인할 예정
        ans = 0 # 출력 할 값
        l = s[i:i+7] # 7비트
        if len(l) != 7: # 마지막에 길이가 7이 아니면
            while len(l) % 7 != 0: # 7 될 때까지
                l = '0'+l # 앞에 0 붙여준다.
        for j in range(7): # 훑으면서
            ans += int(l[j]) * b[j] # 10진수로 변환
        print(f"{ans}", end=' ') # 하나 출력
    print() # 엔터

'''
bii = list(reversed([2**i for i in range(7)]))

def makebi(n):
    if n//2 == 0:
        return str(n%2)
    return makebi(n//2)+str(n/%2)

for testcase in range(1, int(input())+1):
    a = input()
    lena = len(a)
    s = bin(int(a, 16))
    s = s[2:]
    while len(s) != lena*4:
        s = '0'+s
    li = []
    for i in range(0, len(s), 7):
        ans = 0
        l = s[i:i+7]
        if len(l) != 7:
            while len(l) % 7 != 0:
                l = '0'+l
        for j in range(7):
            ans += int(l[j]) * bii[j]
        li.append(ans)
    
    print(f"#{testcase}", end=' ')
    print(*li)
'''






