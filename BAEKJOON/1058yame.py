# 입력 받기
n = int(input())
d = []
for _ in range(n) :
    d.append(list(input()))
# 인덱스 별 친구 목록
fl = [] # 인덱스 별 친구 목록을 2차원으로 생성
for a in d :
    fl.append(list(filter(lambda x: a[x] == "Y", range(len(a)))))
# 이하 개 야매 방법
# d를 0과 1 테이블로 변경
for x in range(n) :
    for y in range(n) :
        if d[x][y] == 'N' :
            d[x][y] = 0
        else : d[x][y] = 1
# 테이블 하나
hap = [[0] * n for _ in range(n)]
# 이 테이블에 자신의 친구와 친구친구 여부를 그대로 더해서 대입
for t in range(len(fl)) :
    for i in fl[t] :
        for j in range(n) :
            hap[t][j] += d[i][j] + d[t][j]
# 친구친구나 친구면 0이 아닌 값이므로 1로 통일
for a in hap :
    for b in range(n) :
        for c in range(n) :
            if hap[b][c] != 0 :
                hap[b][c] = 1
mfn = 0
for d in hap :
    mfn = max(mfn, sum(d))
if mfn == 0 :
    print(mfn)
else :
    print(mfn-1)