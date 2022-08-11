'''
부분집합의 합
1~12 원소 A
부분집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 갯수 출력
없으면 0
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for testcase in range(1, int(input())+1):
    c = 0
    n, k = map(int, input().split())
    for i in range(2 ** 12) :
        h = []
        for j in range(12) :
            if i & (1<<j) :
                h.append(a[j])
        if len(h) == n and sum(h) == k :
            c+=1
    
    print(f"#{testcase} {c}")








