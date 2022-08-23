# SWEA 변형
alp = '0123456789'
ysz = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':3} # 연산자 우선순위 처리용

for testcase in range(1, 11):
    _, s = input(), input()
    ans = '' # 정답
    yz = [] # 연산자들 저장
    for i in s:
        if i in alp: # 숫자면 저장
            ans += i
        else:
            if ysz[i] == 3: # 닫는 괄호
                while yz:
                    a = yz.pop()
                    if ysz[a] == 0: # 여는괄호 처음 만나면
                        break # while을 깨고 나와!
                    ans += a
                continue # while 끝내면 다음 반복
            elif ysz[i] == 0: # 여는 괄호면
                yz.append(i) # 추가하고 끝
                continue
            if yz and ysz[yz[-1]] != 0 and ysz[yz[-1]] > ysz[i]: # 여는괄호가 아니고 우선 순위가 먼저 들어간게 높다면
                while yz and ysz[yz[-1]] != 0: # 비거나 여는괄호 전까지 제거
                    a = yz.pop()
                    ans += a
            elif yz and ysz[yz[-1]] != 0 and ysz[yz[-1]] == ysz[i]: # 여는괄호가 아니고 우선 순위가 동등하다면 즉시 처리한다. 딱 하나만
                a = yz.pop()
                ans+=a
            yz.append(i) # 열고 닫고 우선순위도 이상 없으면 추가해~
    while yz: # 남은거 전부 토해내!
        b = yz.pop()
        ans += b
    # 후위 표현식 계산
    stk = []
    # ysz = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':3}
    for i in ans:
        if i in alp:
            stk.append(int(i))
        else:
            if stk and i == '+':
                stk.append(stk.pop()+stk.pop())
            elif stk and i == '*':
                stk.append(stk.pop() * stk.pop())
            elif stk and i == '-':
                stk.append(-1*stk.pop() + stk.pop())
            elif stk and i == '/':
                stk.append(1/stk.pop() * stk.pop())
    print(ans)
    print(f"#{testcase} {int(stk[0])}")



'''
1+2*5*6
125*6*
'''








