'''
그리디. 설탕배달
'''

n = int(input())

d = [5000] * (5001)
d[3], d[5] = 1, 1
d[4], d[6] = 5000, 2

for i in range(6, n+1):
    if d[i-3] == 5000 and d[i-5] == 5000 :
        continue
    elif d[i-3] != 5000 and d[i-5] == 5000 :
        d[i] = d[i-3] + 1
    elif d[i-3] == 5000 and d[i-5] != 5000 :
        d[i] = d[i-5] + 1
    else :
        d[i] = min(d[i-3], d[i-5]) +1

if d[n] == 5000 :
    print('-1')
else : print(d[n])

'''
d[n]은 d[n-3]과 d[n-5] 중 양수인 작은 값+1
'''