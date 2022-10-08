'''
국회의원 선거.

다솜 1번
다름 모든 사람보다 높아야 당선된다.
매수해야 할 사람 수는?

입력
국회의원수 n
n줄에 받는 수

출력
매수해야 할 사람 최소 명수
'''
n = int(input())
nl = [int(input()) for _ in range(n)]
ds = nl.pop(0)
ans = 0
while nl and max(nl) >= ds:
    nl[nl.index(max(nl))] -= 1
    ds+=1
    ans+=1
print(ans)




