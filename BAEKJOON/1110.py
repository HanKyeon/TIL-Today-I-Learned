'''
더하기 사이클
'''

n = int(input())
re = 1
if n < 10 :
    n *= 10
x, y = n // 10, n % 10
z = x + y
w = y * 10 + z % 10

def plus_cycle(num) :
    global re
    if num == n :
        return re
    re += 1
    a, b = num // 10, num % 10
    c = a + b
    m = b * 10 + c % 10
    return plus_cycle(m)

print(plus_cycle(w))



