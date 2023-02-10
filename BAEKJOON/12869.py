'''
무탈리스크

뮤탈 1개 scv n개.
첫번째 맞은 애는 9, 두번째3, 세번째 1.
scv가 0이 되면 즉시 파괴. 같은 scv 여러번 불가.
남아있는 scv 체력 제시. 모든 scv를 파괴하기 위해 공격해야 하는 횟수의 최솟값.

입력
n 제시.
n개 체력 제시.

출력
scv 파괴하기 위한 공격 횟수의 최솟값
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

if n == 3:
    a, b, c = map(int, input().rstrip().split())
    v = [[[0]*(c+1) for _ in range(b+1)] for _ in range(a+1)]
    q = deque([(a, b, c)])
    v[a][b][c] = 1
    while q:
        a, b, c = q.popleft()
        if a:
            na = 0 if a < 10 else a-9
            if b:
                nb = 0 if b < 4 else b-3
            if c:
                nc = 0 if c < 2 else c-1
            if not v[na][nb][nc]:
                if not na and not nb and not nc:
                    print(v[a][b][c])
                    exit()
                v[na][nb][nc] = v[a][b][c]+1
                q.append((na, nb, nc))
            if c:
                nc = 0 if c < 4 else c-3
            if b:
                nb = 0 if b < 2 else b-1
            if not v[na][nb][nc]:
                if not na and not nb and not nc:
                    print(v[a][b][c])
                    exit()
                v[na][nb][nc] = v[a][b][c]+1
                q.append((na, nb, nc))

        if b:
            nb = 0 if b<10 else b-9
            if a:
                na = 0 if a<4 else a-3
            if c:
                nc = 0 if c<2 else c-1
            if not v[na][nb][nc]:
                if not na and not nb and not nc:
                    print(v[a][b][c])
                    exit()
                v[na][nb][nc] = v[a][b][c]+1
                q.append((na, nb, nc))
            if c:
                nc = 0 if c < 4 else c-3
            if a:
                na = 0 if a < 2 else a-1
            if not v[na][nb][nc]:
                if not na and not nb and not nc:
                    print(v[a][b][c])
                    exit()
                v[na][nb][nc] = v[a][b][c]+1
                q.append((na, nb, nc))

        if c:
            nc = 0 if c < 10 else c-9
            if b:
                nb = 0 if b < 4 else b-3
            if a:
                na = 0 if a < 2 else a-1
            if not v[na][nb][nc]:
                if not na and not nb and not nc:
                    print(v[a][b][c])
                    exit()
                v[na][nb][nc] = v[a][b][c]+1
                q.append((na, nb, nc))
            if a:
                na = 0 if a < 4 else a-3
            if b:
                nb = 0 if b < 2 else b-1
            if not v[na][nb][nc]:
                if not na and not nb and not nc:
                    print(v[a][b][c])
                    exit()
                v[na][nb][nc] = v[a][b][c]+1
                q.append((na, nb, nc))
            
elif n == 2:
    a, b = map(int, input().rstrip().split())
    v = [[0]*(b+1) for _ in range(a+1)]
    q = deque([(a, b)])
    v[a][b] = 1
    while q:
        a, b = q.popleft()
        if a:
            na = 0 if a < 10 else a-9
        if b:
            nb = 0 if b < 4 else b-3
        if not v[na][nb]:
            if not na and not nb:
                print(v[a][b])
                exit()
            v[na][nb] = v[a][b]+1
            q.append((na, nb))
        if b:
            nb = 0 if b < 10 else b-9
        if a:
            na = 0 if a < 4 else a-3
        if not v[na][nb]:
            if not na and not nb:
                print(v[a][b])
                exit()
            v[na][nb] = v[a][b]+1
            q.append((na, nb))
elif n == 1:
    a = int(input())
    ans = a//9+1 if a%9 else a//9
    print(ans)
    exit()



