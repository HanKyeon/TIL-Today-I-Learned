'''
거스름돈

2원 5원짜리로 거스름돈. 동전 갯수 최소가 되도록.

입력
거스름돈 액수 제시

출력
거스름돈 동전 최소 갯수 출력. 못거슬러주면 -1
'''
n = int(input())
if not n%5:
    print(n//5)
    exit()
ans = 0
while n > 0:
    n-=2
    ans += 1
    if not n%5:
        ans += n//5
        break
if n < 0:
    ans = -1
print(ans)








