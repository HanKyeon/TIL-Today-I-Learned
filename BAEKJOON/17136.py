'''
색종이 붙이기

한 변의 길이가 1 2 3 4 5인 색종이 존재.
10*10 종이 위에 붙이려 한다. -> 사이즈가 작아서 맘껏해도 됨.
0 또는 1. 1을 모두 색종이로 붙여야 한다. 경계 밖으로 나갈 수 없고, 겹쳐도 안됨. 칸의 경계와 일치하게 붙여야 한다.

입력
판떼기 제시.
'''
import sys
input=sys.stdin.readline

def func(x, y, cnt):
    global ans
    if y >= 10:
        ans = min(ans, cnt)
        return
    if x >= 10:
        func(0, y+1, cnt)
        return
    if cnt >= ans:
        return
    if a[x][y] == 1:
        for k in range(5):
            if paper[k] == 5:
                continue
            if x + k >= 10 or y + k >= 10:
                continue
            flag = 0
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    if a[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break
            if not flag:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 0
                paper[k] += 1
                func(x + k + 1, y, cnt + 1)
                paper[k] -= 1
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 1
    else:
        func(x + 1, y, cnt)

a = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = sys.maxsize
func(0, 0, 0)
print(ans) if ans != sys.maxsize else print(-1)

'''
# 빠른 코드

import sys
input = sys.stdin.readline

def checkcheck(r, c, count):
    global paper_count, failed
    if count >= paper_count:
        return
    
    if r == 10:
        if count < paper_count:
            paper_count = count
        return
    if c == 0:
        col_check = 0
        for i in range(10):
            if board[r][i]:
                col_check |= 1<<i
        
        if str(papers) in dp[r][col_check]:
            if dp[r][col_check][str(papers)] > count:
                dp[r][col_check][str(papers)] = count
            else:
                return
        else:
            dp[r][col_check][str(papers)] = count
            
    elif c == 10:
        checkcheck(r+1, 0, count)
        return
    
    marked = is_marked(r,c)
    if marked:
        for i in range(1, marked+1):
            if papers[i-1]>0:
                mark(r,c,i,0)
                papers[i-1]-=1
                checkcheck(r,c+i,count+1)
                mark(r,c,i,1)
                papers[i-1]+=1
            else:
                failed = True
    else:
        checkcheck(r,c+1,count)
    return


def is_marked(r,c):
    if board[r][c]:
        if r < 6 and c < 6:
            if sum([sum(board[r+i][c:c+5]) for i in range(5)]) == 25:
                return 5
        if r < 7 and c < 7:
            if sum([sum(board[r+i][c:c+4]) for i in range(4)]) == 16:
                return 4
        if r < 8 and c < 8:
            if sum([sum(board[r+i][c:c+3]) for i in range(3)]) == 9:
                return 3
        if r < 9 and c < 9:
            if sum([sum(board[r+i][c:c+2]) for i in range(2)]) == 4:
                return 2
        return 1
    else:
        return 0

def mark(r,c,size, flag):
    for dr in range(size):
        for dc in range(size):
            board[r+dr][c+dc] = flag
   

board = [list(map(int,input().split())) for _ in range(10)]
papers = [5,5,5,5,5]
dp = [[{} for _ in range(1024)] for _ in range(10)]
paper_count = 30
failed = False
checkcheck(0,0,0)
if paper_count == 30:
    paper_count = 0
if not paper_count and failed:
    print(-1)
else:
    print(paper_count)
'''




'''
def check(h, w, siz):
    if h+siz >= 10 or w+siz >= 10:
        return False
    for i in range(h, h+siz+1):
        for j in range(w, w+siz+1):
            if g[i][j] and not v[h][w]:
                continue
            else:
                return False
    return True

def apl(h, w, siz, val):
    for i in range(h, h+siz+1):
        for j in range(w, w+siz+1):
            v[i][j] = val

g = [list(map(int, input().rstrip().split())) for _ in range(10)]
v = [[0]*10 for _ in range(10)]
pp = [5,5,5,5,5]
ans = int(10e9)
nfla = sum(map(sum, g))

def btc(h, w, cnt):
    global ans, nfla, fla
    if ans <= cnt:
        return
    for i in range(10):
        for j in range(10):
            if not g[i][j] or v[i][j]:
                continue
            for k in range(4, -1, -1):
                if not pp[k]:
                    continue
                a = check(i, j, k)
                if a:
                    apl(i, j, k, 1)
                    pp[k] -= 1
                    nfla -= (k+1)**2
                    s = btc(i, j, cnt+1)
                    nfla += (k+1)**2
                    apl(i, j, k, 0)
                    pp[k] += 1
                else:
                    continue
    if nfla == 0:
        ans = min(ans, cnt)
        return True
btc(0,0,0)
if ans == int(10e9):
    ans = -1
print(ans)
'''







