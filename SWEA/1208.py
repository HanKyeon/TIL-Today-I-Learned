'''
Flatten
'''
# 10회 수행
for t in range(1, 11) :
    #입력
    k = int(input())
    l = list(map(int, input().split()))
    # 최댓값-1 최솟값+1
    for _ in range(k) :
        a = l.index(max(l))
        b = l.index(min(l))
        l[a] = l[a] - 1
        l[b] = l[b] + 1
    # 출력
    print(f"#{t} {max(l) - min(l)}")


