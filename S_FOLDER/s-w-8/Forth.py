'''
Forth

Forth는 스택 연산을 기반으로 한다. 후위연산법 쓴다. 동작은 다음과 같다.

숫자는 스택에 넣는다.
연산자를 만나면 스택 두개를 꺼내 연산하고 결과를 다시 스택에 넣는다.
'.'은 스택에서 숫자를 꺼내 출력한다.
피연산자와 연산자는 여백으로 구분, 코드는 '.'으로 끝남.
나눗셈은 나눠 떨어짐.

입력
테케T
정수/연산자 256자 이내

출력
#테케 계산결과
'''
# 문제가 스레기같네
yz = ['+', '-', '*', '/', '.']
for testcase in range(1, int(input())+1):
    s = input().split()
    print(f"#{testcase}", end=' ')
    ns = []
    for i in s:
        if not i in yz:
            ns.append(int(i))
        else:
            if i == '+':
                if len(ns) < 2:
                    print('error')
                    break
                else:
                    a, b = ns.pop(), ns.pop()
                    ns.append(b+a)
            elif i == '-':
                if len(ns) < 2:
                    print('error')
                    break
                else:
                    a, b = ns.pop(), ns.pop()
                    ns.append(b-a)
            elif i == '*':
                if len(ns) < 2:
                    print('error')
                    break
                else:
                    a, b = ns.pop(), ns.pop()
                    ns.append(a*b)
            elif i == '/':
                if len(ns) < 2:
                    print('error')
                    break
                else:
                    a, b = ns.pop(), ns.pop()
                    ns.append(b//a)
            elif i == '.':
                if len(ns) < 1:
                    print('error')
                    break
                else:
                    print(ns.pop())
