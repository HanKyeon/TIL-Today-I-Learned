# 1부터99까진 전부 한수
# d = [111, 123, 135, 147, 159, 222, 234, 246, 258, 333, 345, 357, 369, 444, 456, 468, 555, 567, 579, 666, 678, 777, 789]
# 숫자를 받고, (1,숫자+1)만큼의 range를 순회
# 순회 하면서 리스트화해서 길이가 1이면 그 숫자만큼 더하고
# 리스트의 길이가 2 이상이면 c가 9부터 시작
# 0인덱스와 1인덱스의 차이 d를 기준으로 0인덱스와 1인덱스 차이 비교
# 최대길이까지 이전 것과 반복하여 d와 다르면 컨티뉴 같으면 c+=1

# 10000 이상에서도 가능하도록 하려면?
n = int(input())
c = 0

if 1 <= n <= 99 :
    c += n
elif n < 0 :
    c = 0
else :
    c = 99

if 100 <= n <= 1000 :
    for i in range(100, n+1) :
        N = list(map(int, list(str(i))))
        if N[2] - N[1] == N[1] - N[0] :
            c += 1

print(c)


# n[i+1] - n[i] = n[i] - n[i-1] = ...
