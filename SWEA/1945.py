'''
간단한 소인수분해
'''
for testcase in range(1, int(input())+1) :
    n = int(input())
    nl = [2, 3, 5, 7, 11]
    li = [0] * 5
    for i in range(5) :
        while n % nl[i] == 0 :
            n //= nl[i]
            li[i] += 1
    print(f"#{testcase}", *li)


'''
for testcase in range(1, int(input())+1) :
    n = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while n % 2 == 0 :
        n = n // 2
        a += 1
    while n % 3 == 0 :
        n = n // 3
        b += 1
    while n % 5 == 0 :
        n = n // 5
        c += 1
    while n % 7 == 0 :
        n = n // 7
        d += 1
    while n % 11 == 0 :
        n = n // 11
        e += 1
    print(f"#{testcase} {a} {b} {c} {d} {e}")

'''