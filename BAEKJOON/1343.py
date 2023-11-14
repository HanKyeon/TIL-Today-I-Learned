'''
폴리오미노

AAAA BB 무한대.
X를 모두 덮을 것. 모두 덮은 보드판 출력.
.은 못덮음

입력
보드판 제시

출력
사전순으로 가장 앞서는 답 출력
'''
l = input().rstrip().split('.')
ans = ''
def check():
    global l, ans
    for i in l:
        if len(i)%2: return -1
        ans += 'AAAA'*(len(i)//4) + ('BB.' if len(i)%4 else '.')

a = check()
print(a if a else ans[:-1])

