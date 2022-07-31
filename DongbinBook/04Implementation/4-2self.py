'''
시각
00:00:00에서부터 n:59:59까지 모든 시각 중 3이 포함되어 있으면 카운트
'''

n = int(input())

d = []

c = 0 

for s in range(24) :
    for b in range(60) :
        for ch in range(60) :
            if '3' in str(s) or '3' in str(b) or '3' in str(ch) :
                c += 1
    d.append(c)

print(d)
print(d[n])

# 1초에 2000만번의 연산!!!!!!!!!!!!!!!!!