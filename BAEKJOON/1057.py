# 입력
n, k, i = map(int, input().split())
c = 0 # 카운트
# 같아질 때 (대결 할 때)까지 반복
while k != i :
    # 번호는 반씩 줄어든다.
    k -= k//2
    i -= i//2
    c += 1

print(c)


