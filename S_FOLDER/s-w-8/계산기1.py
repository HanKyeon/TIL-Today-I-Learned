'''
계산기1.
후위표기법으로 변환하기.
'''
sz, yz = '0123456789', '+*'

for testcase in range(1, int(input())+1):
    
    s = input()
    szs, yzs = [], []
    ans = ''
    for i in s:
        if i in sz:
            ans += i
            szs.append(i)
        elif i in yz:
            if yzs and yzs[-1] == '+' and i == '+':
                ans += yzs.pop()
            elif yzs and yzs[-1] == '*' and i == '+':
                while yzs:
                    ans += yzs.pop()
            elif yzs and yzs[-1] == '*' and i == '*':
                ans += yzs.pop()
            yzs.append(i)
    while yzs:
        ans += yzs.pop()
    print(f"#{testcase} {ans}")

#1 952*+1+33*7*6*+