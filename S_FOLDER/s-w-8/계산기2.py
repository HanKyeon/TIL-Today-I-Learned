'''
계산기2
'''
sz, yz = '0123456789', '+*'

for testcase in range(1, 11):
    _ = input()
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
    valans = 0
    val = []
    for i in ans:
        if i in sz:
            val.append(int(i))
        elif i == '*':
            a, b = val.pop(), val.pop()
            val.append(a*b)
        elif i == '+':
            c, d = val.pop(), val.pop()
            val.append(c+d)
    print(f"#{testcase} {val[0]}")

