'''
종이 붙이기
20*20 20*10 종이로 
'''
g =[0, 1, 3]+[0]*28

for i in range(3, 31):
    # g[i] = g[i-2]*2 + g[i-1] # 점화식1 3부터 돌려야 함
    if i % 2 == 0: # 점화식2 2부터 돌려도 됨
        g[i] = g[i-1]*2+1
    if i % 2 == 1:
        g[i] = g[i-1]*2-1
for testcase in range(1, int(input())+1):print(f"#{testcase} {g[int(input()) // 10]}")
