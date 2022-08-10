'''
부분집합 합
'''
def ps(li) :
    n = len(li)
    for i in range(1<<n) :
        c = -1
        for j in range(n) :
            if i & (1 << j) :
                c+=li[j]
                if c == 0 :
                    return 1
    return 0

for testcase in range(1, int(input())+1) :
    print(f"#{testcase}", end=' ')
    print(ps(list(map(int, input().split()))))
'''
2
19 6 16 19 15 16 8 13 16 10
-20 -6 -13 3 -19 -9 19 -3 9 4
'''

print(range(1<<4))

# 질문1. 1 << n 대신에 2 ** n 을 써도 되는건지? ㅇㅇ
# 질문2. i & (1 << j) 라는게 i의 j번째 비트가 1인지 아닌지 검사한다 하였는데 어떤식으로 되는건지

for testcase in range(1, int(input())+1) :
    lst = list(map(int, input().split()))
    ans = 0
    k = 0
    N = len(lst) # N 비트이다.
    # 삼성 전자 같은 경우 유난히 비트 쪽을 하드웨어 가전 휴대폰 그런데라 좀 많다.
    # 재귀는 재귀대로 알아야 하지만 비트도 비트대로 알아야 한다.

    for bit in range(1, 2**N) :
        sm = 0
        for i in range(0, N) :
            if (bit>>i) & 1 :
                sm += lst[i]
        if sm == k :
            ans += 1







