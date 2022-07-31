'''
곱하기 혹은 더하기
'''
n = input()

nl = list(map(int, list(n)))
bn = 0

for i in nl :
    if i == 0 or i == 1 or bn == 0 or bn == 1:
        bn += i
    else :
        bn *= i

print(bn)