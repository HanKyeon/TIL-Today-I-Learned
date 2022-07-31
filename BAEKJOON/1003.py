'''
피보나치 시간 줄이기 dp
'''

d = [[0] * 2 for _ in range(41)]
d[0][0] = 1
d[1][1] = 1

for i in range(2, len(d)) :
    d[i][0] = d[i-2][0] + d[i-1][0]
    d[i][1] = d[i-2][1] + d[i-1][1]

for t in range(int(input())) :
    n = int(input())
    print(f"{d[n][0]} {d[n][1]}")
