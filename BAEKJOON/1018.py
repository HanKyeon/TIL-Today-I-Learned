'''
체스판 다시 칠하기
'''
n, m = map(int, input().split())
chesspan = []

for i in range(m) :
    chesspan.append(list(input()))

print(chesspan)

for a in range(n - 7) :
    if a == 'W' :
        for b in range(m - 7) :
            pass
    else : 
        for b in range(m - 7) :
            pass

        


'''
완탐. 어차피 최대가 50 50이니가 걍 for문 돌려도 될듯

W로 시작하는 체스판
B로 시작하는 체스판

WBWBWBWB
BWBWBWBW
'''
