'''
기상캐스터
H, W
c는 구름.은 그냥 칸

입력
H, W
C는 구름 .은 그냥 지역

출력
구름이 언제 오는지. 못오면 -1
'''
h, w = map(int, input().split()) # hw
g = [[-1] * w for _ in range(h)] # 그래프
for i in range(h): # 순회
    s = input() # 입력 받은거
    for j in range(w): # 돌면서
        if s[j] == 'c': # c 만나면 0으로 초기화
            g[i][j] = 0 # c 아니면서 j가 1이상이고 j-1이 0이상이면
        elif j>0 and g[i][j-1]>=0: # 1 더해준다.
            g[i][j] = g[i][j-1]+1
for i in g: # 출력
    print(*i)

