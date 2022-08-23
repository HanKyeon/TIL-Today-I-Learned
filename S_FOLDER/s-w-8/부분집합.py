'''
부분집합

n은 1~12 k는 1~100
'''
'''
for testcase in range(1, int(input())+1):
    n, k = map(int, input().split())
    nl = list(map(int, input().split()))
    ans = 0
    for i in range(2**n):
        bb = []
        for j in range(n):
            if i & (1<<j):
                bb.append(nl[j])
        if sum(bb) == k:
            ans += 1
    print(f"#{testcase} {ans}")
'''

def 부분집합(s, num, i, li):
    global n, ans
    if s > k:
        return
    if num == n:
        if s == k:
            ans += 1
            print(li)
        return
    num += 1
    li[i] = nl[i]
    s = sum(li)
    부분집합(s, num, i+1, li)
    li[i] = 0
    s = sum(li)
    부분집합(s, num, i+1, li)

for testcase in range(1, int(input())+1):
    n, k = map(int, input().split())
    nl = list(map(int, input().split()))
    ans = 0
    l = [0] * len(nl)
    부분집합(0, 0, 0, l)
    print(f"#{testcase} {ans}")



