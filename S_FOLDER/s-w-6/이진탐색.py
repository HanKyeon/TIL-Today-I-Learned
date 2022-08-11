# 일반 이진탐색
def bs(sta, end, num) :
    c = 0
    while sta <= end :
        c += 1
        mid = int((sta + end) / 2)
        if pg[mid] == num :
            return c
        elif num > pg[mid] :
            sta = mid + 1
        elif num < pg[mid] :
            end = mid - 1
    return c
# 재귀 이진탐색
def bs2(sta, end, num, c) :
    while sta <= end :
        c += 1
        mid = int((sta + end) / 2)
        if pg[mid] == num :
            return c
        elif num > pg[mid] :
            return bs2(mid+1, end, num, c)
        elif num < pg[mid] :
            return bs2(sta, mid-1, num, c)
# 몸체
for testcase in range(1, int(input())+1) :
    # 입력
    p, pa, pb = map(int, input().split())
    pg = list(range(p+1))
    a, b = bs(1, p, pa), bs(1, p, pb)
    print(f"#{testcase}", end=' ')
    if a < b :
        print("A")
    elif a > b :
        print("B")
    else: print('0')
'''
    a, b = bs2(1, p, pa, 0), bs2(1, p, pb, 0)
    print(f"#{testcase}", end=' ')
    if a < b :
        print("A")
    elif a > b :
        print("B")
    else: print('0')
'''

