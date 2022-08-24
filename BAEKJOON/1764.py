'''
듣보잡

입력
듣도못한사람 수 N 보도 못한 사람 수 M 50만 이하 자연수
듣못
보못

출력
듣보잡의 수
명
단
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
d, b = set(), set()
for i in range(n):
    s = input().rstrip()
    d.add(s)
for i in range(m):
    s = input().rstrip()
    b.add(s)
db = sorted(list(d&b))

print(len(db))
for i in db:
    print(i)



