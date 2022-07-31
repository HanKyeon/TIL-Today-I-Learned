'''
친구 bfs
'''
# 입력 및 그래프로 만들기
from collections import deque


n = int(input())
d = []
for _ in range(n) :
    d.append(list(input()))

# 인덱스 별 친구 목록
fl = []
for a in d :
    fl.append(list(filter(lambda x: a[x] == "Y", range(len(a)))))

def bfs(idx, dep) :
    q = deque()
    fc = [0] * n
    fc[idx] = 1
    q.append((idx, dep))
    
    while q :
        nidx, nc = q.popleft()
        for i in fl[nidx] :
            if nc < 2 :
                if fc[i] != 1 :
                    fc[i] = 1
                    q.append((i, nc+1))

    return fc.count(1)

mfn = 0

for i in range(n) :
    nfn = bfs(i,0)
    mfn = max(mfn, nfn)

print(mfn - 1)


