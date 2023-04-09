'''
인공지능 시계

끝나는 시각 계산.

입력
a, b, c 시분초 제시.
필요한 시간 d 제시.

출력
종료되는 시각 시 분 초 제시. 시는 0부터 23 정수, 분 초는 0부터 59 사이 정수. 24 00 00은 0 0 0이다.
'''
a, b, c = map(int, input().rstrip().split())
d = int(input()) % 86400
ali = []
for i in [3600, 60, 1]:
    j = d // i
    d %= i
    ali.append(j)
a += ali[0]
b += ali[1]
c += ali[2]
if c >=60:
    c %= 60
    b += 1
if b >= 60:
    b %= 60
    a += 1
if a>= 24:
    a %= 24
print(a,b,c)




