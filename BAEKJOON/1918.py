'''
후위 표기식

중위표기식이 주어졌을 때 후위표기식으로 고치는 프로그램 작성.

입력
중위표기식 제시. 피연산자는 알파벳 대문자. 표기식은 +-*/()로만 제시

출력
후위표기식으로 바뀐 식 제시
'''

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = input()
ysz = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':3} # 연산자 우선순위 처리용
yz = [] # 연산자들 저장
ans = '' # 정답
for i in s: # 문자 순회하면서
    if i in alp: # 연산자 아니면
        ans += i # 정답에 붙여줌
    else:
        if ysz[i] == 3: # 닫는 괄호
            while yz:
                a =  yz.pop()
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
        elif yz and ysz[yz[-1]] != 0 and ysz[yz[-1]] == ysz[i]: # 여는괄호가 아니고 우선 순위가 동등하다면 즉시 처리한다.
            a = yz.pop()
            ans+=a
        yz.append(i) # 열고 닫는거 아니면 추가해~
while yz: # 남은거 전부 토해내!
    b = yz.pop()
    ans += b
print(ans)



# SWEA 변형
alp = '0123456789'
s = input()
ysz = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':3} # 연산자 우선순위 처리용
yz = [] # 연산자들 저장

for testcase in range(1, int(input())+1):
    ans = '' # 정답
    for i in s: # 문자 순회하면서
        if i in alp: # 연산자 아니면
            ans += i # 정답에 붙여줌
        else:
            if ysz[i] == 3: # 닫는 괄호
                while yz:
                    a =  yz.pop()
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
            elif yz and ysz[yz[-1]] != 0 and ysz[yz[-1]] == ysz[i]: # 여는괄호가 아니고 우선 순위가 동등하다면 즉시 처리한다.
                a = yz.pop()
                ans+=a
            yz.append(i) # 열고 닫는거 아니면 추가해~
    while yz: # 남은거 전부 토해내!
        b = yz.pop()
        ans += b
    print(f"#{testcase} {ans}")



