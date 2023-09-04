'''
수리공 항승

길이 L인 테이프 무제한. 좌측에서 정수만큼 떨어진 거리만 물이 샌다.
물을 막을 때 0.5 간격을 줘야 물이 다시 안샌다. 필요한 테이프의 최소 갯수 구해라. 자르기 겹치기 가능

입력
n, l 제시. 1000이하 자연수
물 새는 곳 제시 1000이하 자연수

출력
필요한 테이프 갯수
'''
import sys
input = sys.stdin.readline

_, l = map(lambda x: int(x)-1, input().rstrip().split())
nl = list(sorted(map(int, input().rstrip().split())))

nod, cnt = nl.pop(0), 1
while nl:
    try:
        while nl[0] <= nod+l: nl.pop(0)
    except: break
    nod = nl.pop(0)
    cnt+=1
print(cnt)

'''
# 숏코딩
n,l,*a=map(int,open(0).read().split())
c=1
y,*a=sorted(a)
for x in a:
 if x-y>=l:y=x;c+=1
print(c)
'''
