'''
책 페이지

전체 페이지 수가 n인 책 하나 있음. 1부터 n. 각 숫자가 전체 페이지 번호에서 모두 몇 번 나오는지 구하시오

입력
n 제시 10억 이하

출력
0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, 9가 총 몇 번 나오는지 공백 구분 출력
'''
n = int(input())
ans = [0]*10

for i in range(len(str(n))):
    num = n//10*10+9-n
    for j in range(10):
        ans[j] += (n//10+1) * 10**i
    for j in range(10-num, 10):
        ans[j] -= 10**i
    for j in str(n)[:-1]:
        ans[int(j)] -= num * 10**i
    ans[0] -= 10**i
    n //= 10

print(*ans)

# 빠르고 짧다!
a=[0]*10;n=int(s:=input());f=1
for _ in s:
 for i in range(10):v=f*10;a[i]+=(n//v-(i<1))*f+min(max(n%v+1-i*f,0),f)
 f=v
print(*a)
