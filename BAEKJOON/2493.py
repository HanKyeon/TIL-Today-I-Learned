'''
탑

탑 갯수 n과 탑들의 높이 제시.
각각의 탑에서 발사한 신호를 어디서 수신하는지 알아내라.

입력
탑 갯수 n 제시. 1이상 50만 이하.
n개 탑 높이 한 줄 제시. 높이는 1이상 1억 이하

출력
주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈 칸 사이에 두고 출력. 레이저 ㅅ니호를 수신하는 탑이 존재하지 않으면 0 출력.
'''
import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().rstrip().split()))
idxs = list(range(n))
stk = []
ans = [0]*n
while idxs:
    a = idxs.pop()
    aval = nl[a]
    while stk and nl[stk[-1]] <= aval:
        ans[stk.pop()] = a+1
    stk.append(a)

print(*ans)



