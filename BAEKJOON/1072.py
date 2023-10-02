'''
게임

게임 횟수 x
이긴 게임 Y, z% 승률 소수점 버림
X와 Y 제시, 게임 최소 몇 번 더 해야 Z가 변하는지
'''
def check(mid):
    global x, y, z
    return int((y+mid)*100/(x+mid)) != z

x, y = map(int, input().rstrip().split())
z = int(y*100/x)
l, r = 0, x
ans = 1111111111

while l<=r:
    mid = (l+r)//2
    print(f"mid : {mid}, zValue : {int((y+mid)/(x+mid)*100)}")
    if check(mid):
        if ans > mid: ans = mid
        r = mid-1
        continue
    l = mid+1
print(ans if ans != 1111111111 else -1)



